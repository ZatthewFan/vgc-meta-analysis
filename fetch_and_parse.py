from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from modules.pokemon import Pokemon
from modules.team import Team
import re
import requests

class FetchFromURL:
    BASE_URL = None
    CURRENT_FORMAT = None

    options = Options()
    options.add_argument("load-extension=./extensions/ublock-origin")
    driver = webdriver.Chrome(options=options)
    
    pokedex = None

    def __init__(self, base_url: str, format: str) -> None:
        self.BASE_URL = base_url
        self.CURRENT_FORMAT = format
        self.pokedex = self.fetch_pokedex()
    
    def open_webpage(self) -> None:
        self.driver.get(self.BASE_URL)

    def get_pokepaste_links(self) -> list[str]:
        pokepastes = []
        pokepaste_links = self.driver.find_elements(By.XPATH, '//a[contains(@href, "pokepast.es")]')
        for link in pokepaste_links:
            pokepastes.append(link.get_attribute('href'))
        
        return pokepastes

    def parse_ev_iv(self, which: str, pkm: Pokemon, stats: list[str]) -> None:
        stats_dict = {}
        for stat in stats:
            stat = stat.strip()
            stat = stat.split()
            stats_dict[stat[1]] = int(stat[0])
        
        if which == "ev":
            for item in stats_dict.items():
                key = item[0].lower()
                value = item[1]
                pkm.set_ev(**{key: value})
        elif which == "iv":
            for item in stats_dict.items():
                key = item[0].lower()
                value = item[1]
                pkm.set_iv(**{key: value})

    def parse_moveset(self, pkm: Pokemon, moves: WebElement) -> None:
        moveset = []
        
        # getting rid of extra spaces and hyphens
        for move in moves:
            # extra check to see if it's actually a move
            if move[:2] != "- ":
                continue
            move = move.split("- ")[1]
            move = move.strip()
            moveset.append(move)
        
        pkm.set_moveset(moveset)

    # this was a headache 😵‍💫
    def parse_mon(self, pkm_set: WebElement, team: Team) -> Pokemon:
        pkm = Pokemon()
        pkm_set = pkm_set.text.splitlines()
        
        # name, item, and ability are sure to be in the pokepaste
        pkm.set_name(pkm_set[0].split("@")[0].strip())
        try:
            pkm.set_item(pkm_set[0].split("@")[1].strip())
        except IndexError:
            pkm.set_item(None)
        pkm.set_ability(pkm_set[1].split(":")[1].strip())
        
        # for smogon formats
        if "vgc" not in self.CURRENT_FORMAT:
            pkm.set_level(100)
        
        # Tera Type, EVs, Nature, and IVs might not be in the pokepaste or might not be in a fixed line
        # this loops through every line, checking whether it's any of the attributes we're looking for, and updates the pokemon set
        for i in range(2, len(pkm_set)):
            line = pkm_set[i]
            
            if "Tera Type" in line:
                pkm.set_tera(line.split(":")[1].strip())
            elif "EVs" in line:
                self.parse_ev_iv("ev", pkm, re.split(": | / ", line)[1:])
                team.set_ots(False)
            elif "Nature" in line:
                pkm.set_nature(line.split()[0].strip())
            elif "IVs" in line:
                self.parse_ev_iv("iv", pkm, re.split(": | / ", line)[1:])
        
        if not team.is_ots:
            # keys are all lowercase, no spaces, no forme hyphens, and no gender indication outside of formes
            # for example: Ogerpon-Hearthflame (F) -> ogerponhearthflame
            dex_info = self.pokedex[pkm.get_name().lower().replace(" ", "").replace("-", "")]
            pkm.set_dex_info(dex_info)
            
            # set total stats after parsing of nature, iv, and ev has finished to avoid errors
            pkm.set_total_stats()
        
        # last 4 lines are probably the moves
        self.parse_moveset(pkm, pkm_set[-4:])
        
        return pkm

    def parse_pokepaste(self) -> Team:
        sets = self.driver.find_elements(By.CSS_SELECTOR, 'pre')
        try:
            vgc_format = self.driver.find_element(By.CSS_SELECTOR, 'aside p').text[8:]
        except NoSuchElementException:
            vgc_format = "N/A"
        
        team = Team(vgc_format)
        
        if (vgc_format != self.CURRENT_FORMAT):
            return
        
        for pkm_set in sets:
            pkm = self.parse_mon(pkm_set, team)
            team.add_pkm(pkm)
            
        return team

    def parse_all_pokepastes(self, pokepastes: list[str]) -> list[Team]:
        teams = []
        for pokepaste in pokepastes:
            self.driver.get(pokepaste)
            paste = self.parse_pokepaste()
            if paste == None:
                continue
            
            teams.append(paste)
        return teams

    def fetch_pokedex(self) -> dict:
        # showdown's api >>>> pokeapi
        base_url = f"https://play.pokemonshowdown.com/data/pokedex.json"
        response = requests.get(base_url)
        
        if response.status_code != 200:
            print(f"error: {response.status_code}")
            
        return response.json()

    def fetch(self) -> list[Team]:
        self.open_webpage()
        pokepastes = self.get_pokepaste_links()
        teams = self.parse_all_pokepastes(pokepastes)
        self.driver.quit()
        return teams

if __name__ == "__main__":
    url_fetcher = FetchFromURL("https://victoryroadvgc.com/sv-rental-teams/", "gen9vgc2023regulatione")
    teams = url_fetcher.fetch()
    print("success!")