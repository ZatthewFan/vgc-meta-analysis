from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from Pokemon import Pokemon
from Team import Team
import re

BASE_URL = "https://victoryroadvgc.com/sv-rental-teams-2023/"
# BASE_URL = "https://docs.google.com/spreadsheets/d/1axlwmzPA49rYkqXh7zHvAtSP-TKbM0ijGYBPRflLSWw/edit#gid=1948547929"
CURRENT_FORMAT = "gen9vgc2023regulatione"

options = Options()
options.add_argument("load-extension=./extensions/ublock-origin")
driver = webdriver.Chrome(options=options)

def open_webpage():
    driver.get(BASE_URL)

# returns a list of all links containing pokepast.es
def get_pokepaste_links():
    pokepastes = []
    pokepaste_links = driver.find_elements(By.XPATH, '//a[contains(@href, "pokepast.es")]')
    for link in pokepaste_links:
        pokepastes.append(link.get_attribute('href'))
    
    return pokepastes

# helper function to process the ev and iv 
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

def parse_moveset(pkm, moves):
    moveset = []
    
    # getting rid of extra spaces and hyphens
    for move in moves:
        move = move.split("-")[1]
        move = move.strip()
        moveset.append(move)
    
    pkm.set_moveset(moveset)

# parses the data for each individual pokemon
def parse_mon(pkm_set, team):
    pkm = Pokemon()
    pkm_set = pkm_set.text.splitlines()

    if "EV" not in pkm_set[4]:
        return
    
    # name, item, and ability are sure to be in the pokepaste
    pkm.set_name(pkm_set[0].split("@")[0].strip())
    pkm.set_item(pkm_set[0].split("@")[1].strip())
    pkm.set_ability(pkm_set[1].split(":")[1].strip())
    
    # Tera Type, EVs, Nature, and IVs might not be in the pokepaste or might not be in a fixed line
    # this loops through every line, checking whether it's any of the attributes we're looking for, and updates the pokemon set
    for line in pkm_set:
        if "Tera Type" in line:
            pkm.set_tera(line.split(":")[1].strip())
        elif "EVs" in line:
            parse_ev_iv("ev", pkm, re.split(": |/", line.strip())[1:])
            team.set_ots(False)
        elif "Nature" in line:
            pkm.set_nature(line.split()[0].strip())
        elif "IVs" in line:
            parse_ev_iv("iv", pkm, re.split(": |/", line.strip())[1:])
    
    # last 4 lines are definitely the moves
    parse_moveset(pkm, pkm_set[-4:])
    
    return pkm

# stratifies the pokepaste for each pokemon, and iterates through them
def parse_pokepaste():
    sets = driver.find_elements(By.CSS_SELECTOR, 'pre')
    try:
        vgc_format = driver.find_element(By.CSS_SELECTOR, 'aside p').text[8:]
    except NoSuchElementException:
        vgc_format = "N/A"
    team = Team(vgc_format)
    
    # format checker
    if (vgc_format != CURRENT_FORMAT):
        return
    
    for pkm_set in sets:
        pkm = parse_mon(pkm_set, team)
        if pkm == None:
            continue
        
        team.add_pkm(pkm)
        
    
    return team


def parse_all_pokepastes(pokepastes):
    teams = []
    for pokepaste in pokepastes:
        driver.get(pokepaste)
        paste = parse_pokepaste()
        if paste == None:
            continue
        
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
    parse_moveset(pkm, set[-4:])
    print(pkm.get_moveset())

def fetch_from_url():
    open_webpage()
    pokepastes = get_pokepaste_links()
    teams = parse_all_pokepastes(pokepastes)
    return teams

def pkm_to_df(teamlist):
    for pkm in teamlist:
        print("test") #TODO this is a placeholder; change this
    return

def team_to_df(team):
    pkm_to_df(team.get_teamlist())
    return

def teams_to_csv(teams):
    # TODO decide whether teams are supposed to be a csv referencing other csv for pokemon, directory, or teams and pokemon should be in different diretories
    for team in teams:
        team_to_df(team)
    return

if __name__ == "__main__":
    teams = fetch_from_url()
    
    # teams_to_csv(teams)
    driver.quit()
    
    # testing()