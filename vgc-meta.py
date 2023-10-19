from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from Pokemon import Pokemon
from Team import Team
import re

BASE_URL = "https://victoryroadvgc.com/sv-rental-teams-2023/"
CURRENT_FORMAT = "gen9vgc2023regulatione"

options = Options()
options.add_argument("load-extension=./extensions/ublock-origin")
driver = webdriver.Chrome(options=options)

pokepastes = []

def open_webpage():
    driver.get(BASE_URL)

def get_pokepaste_links():
    pokepaste_links = driver.find_elements(By.XPATH, '//a[contains(@href, "pokepast.es")]')
    for link in pokepaste_links:
        pokepastes.append(link.get_attribute('href'))

def parse_ev_iv(which, pkm, stats):
    stats_dict = {}

    for stat in stats:
        stat = stat.strip()
        stat = stat.split()
        stats_dict[stat[1]] = int(stat[0])
    
    if which == "ev":
        for item in stats_dict.items():
            key = item[0]
            value = item[1]
            pkm.set_ev(**{key: value})
    elif which == "iv":
        for item in stats_dict.items():
            key = item[0]
            value = item[1]
            pkm.set_iv(**{key: value})

def parse_moveset(pkm, *args):
    if len(args) > 4:
        return
    
    moveset = []
    
    for move in args:
        move = move.split("-")[1]
        move = move.strip()
        moveset.append(move)
    
    pkm.set_moveset(moveset)

def parse_mon(pkm_set):
    pkm = Pokemon()
    pkm_set = pkm_set.text.splitlines()

    if "EV" not in pkm_set[4]:
        return
    
    pkm.set_name(pkm_set[0].split("@")[0].strip())
    pkm.set_item(pkm_set[0].split("@")[1].strip())
    pkm.set_ability(pkm_set[1].split(":")[1].strip())
    pkm.set_tera(pkm_set[3].split(":")[1].strip())
    parse_ev_iv("ev", pkm, re.split(": |/", pkm_set[4].strip())[1:])
    pkm.set_nature(pkm_set[5].split()[0].strip())
    if "IV" in pkm_set[6]:
        parse_ev_iv("iv", pkm, re.split(": |/", pkm_set[6].strip())[1:])
        parse_moveset(pkm, pkm_set[7], pkm_set[8], pkm_set[9], pkm_set[10])
    else:
        parse_moveset(pkm, pkm_set[6], pkm_set[7], pkm_set[8], pkm_set[9])
    return pkm

def parse_pokepaste():
    sets = driver.find_elements(By.CSS_SELECTOR, 'pre')
    vgc_format = driver.find_element(By.CSS_SELECTOR, 'aside p').text[8:]
    team = Team(vgc_format)
    
    if (vgc_format != CURRENT_FORMAT):
        return
    
    for pkm_set in sets:
        pkm = parse_mon(pkm_set)
        if pkm == None:
            continue
        
        team.add_pkm(pkm)
        
    
    return team


def parse_all_pokepastes():
    teams = []
    for pokepaste in pokepastes:
        driver.get(pokepaste)
        paste = parse_pokepaste()
        if paste == None:
            break
        
        teams.append(paste)
    return teams


def testing():
    url = "https://pokepast.es/22b07255f896b829"
    
    driver.get(url)
    set = driver.find_element(By.XPATH, '/html/body/article[1]/pre').text.splitlines()
    
    print(set[0].split("@")[0].strip())
    print(set[0].split("@")[1].strip())
    print(set[1].split(":")[1].strip())
    print(set[3].split(":")[1].strip())
    print(re.split(": |/", set[4])[1:])
    print(set)
    
    pkm = Pokemon()
    parse_ev_iv("ev", pkm, re.split(": |/", set[4])[1:])
    parse_moveset(pkm, set[7], set[8], set[9], set[10])
    print(pkm.get_moveset())

def teams_to_csv(teams):
    # TODO complete
    return

def main():
    open_webpage()
    get_pokepaste_links()
    teams = parse_all_pokepastes()
    
    teams_to_csv(teams)
    driver.quit()
    
    # testing()

main()