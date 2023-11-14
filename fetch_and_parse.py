from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
import pandas as pd
from modules.pokemon import Pokemon
from modules.team import Team
import re

class FetchFromURL:
    BASE_URL = None
    CURRENT_FORMAT = None

    options = Options()
    options.add_argument("load-extension=./extensions/ublock-origin")
    driver = webdriver.Chrome(options=options)

    def __init__(self, base_url: str, format: str) -> None:
        self.BASE_URL = base_url
        self.CURRENT_FORMAT = format
    
    def open_webpage(self) -> None:
        self.driver.get(self.BASE_URL)

    # returns a list of all links containing pokepast.es
    def get_pokepaste_links(self) -> list[str]:
        pokepastes = []
        pokepaste_links = self.driver.find_elements(By.XPATH, '//a[contains(@href, "pokepast.es")]')
        for link in pokepaste_links:
            pokepastes.append(link.get_attribute('href'))
        
        return pokepastes

    # helper function to process the ev and iv 
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

    # parses the data for each individual pokemon
    def parse_mon(self, pkm_set: WebElement, team: Team) -> Pokemon:
        pkm = Pokemon()
        pkm_set = pkm_set.text.splitlines()

        # if "EV" not in pkm_set[4]:
        #     return
        
        # name, item, and ability are sure to be in the pokepaste
        pkm.set_name(pkm_set[0].split("@")[0].strip())
        pkm.set_item(pkm_set[0].split("@")[1].strip())
        pkm.set_ability(pkm_set[1].split(":")[1].strip())
        
        # Tera Type, EVs, Nature, and IVs might not be in the pokepaste or might not be in a fixed line
        # this loops through every line, checking whether it's any of the attributes we're looking for, and updates the pokemon set
        for i in range(2, len(pkm_set)):
            line = pkm_set[i]
            
            if "Level" in line:
                pkm.set_level(int(line.split(":")[1].strip()))
            elif "Tera Type" in line:
                pkm.set_tera(line.split(":")[1].strip())
            elif "EVs" in line:
                self.parse_ev_iv("ev", pkm, re.split(": | / ", line)[1:])
                team.set_ots(False)
            elif "Nature" in line:
                pkm.set_nature(line.split()[0].strip())
            elif "IVs" in line:
                self.parse_ev_iv("iv", pkm, re.split(": | / ", line)[1:])
        
        # last 4 lines are probably the moves
        self.parse_moveset(pkm, pkm_set[-4:])
        
        return pkm

    # stratifies the pokepaste for each pokemon, and iterates through them
    def parse_pokepaste(self) -> Team:
        sets = self.driver.find_elements(By.CSS_SELECTOR, 'pre')
        try:
            vgc_format = self.driver.find_element(By.CSS_SELECTOR, 'aside p').text[8:]
        except NoSuchElementException:
            vgc_format = "N/A"
        
        team = Team(vgc_format)
        
        # format checker
        if (vgc_format != self.CURRENT_FORMAT):
            return
        
        for pkm_set in sets:
            pkm = self.parse_mon(pkm_set, team)
            
            # # if pkm is does not have ev
            # if pkm == None:
            #     continue
            
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

    def fetch(self) -> list[Team]:
        self.open_webpage()
        pokepastes = self.get_pokepaste_links()
        teams = self.parse_all_pokepastes(pokepastes)
        self.driver.quit()
        return teams


class ConvertCSV:
    def pkm_to_df(self, teamlist):
        n = 0           # test purposes; remove later
        for pkm in teamlist:
            print(n)    # TODO this is a placeholder; change this
            n += 1      # test purposes; remove later
        return

    def team_to_df(self, team: Team) -> None:
        self.pkm_to_df(team.get_teamlist())
        # do something with team format
        # do something with team OTS status
        return

    def teams_to_csv(self, teams: list[Team]) -> None:
        # TODO decide whether teams are supposed to be a csv referencing other csv for pokemon, directory, or teams and pokemon should be in different diretories
        for team in teams:
            self.team_to_df(team)
        return

if __name__ == "__main__":
    url_fetcher = FetchFromURL("https://victoryroadvgc.com/sv-rental-teams-2023/", "gen9vgc2023regulatione")
    teams = url_fetcher.fetch()
    
    converter = ConvertCSV()
    converter.teams_to_csv(teams)