from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import pokemon

BASE_URL = "https://victoryroadvgc.com/sv-rental-teams-2023/"

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

def parse_pokepaste():
    # name = None
    # item = None
    # ability = None
    # tera = None
    # ev = {
    #     "HP" : 0, 
    #     "Atk": 0, 
    #     "Def": 0, 
    #     "SpA": 0, 
    #     "SpD": 0, 
    #     "Spe": 0
    # }
    # nature = None
    # iv = {
    #     "HP" : 31, 
    #     "Atk": 31, 
    #     "Def": 31, 
    #     "SpA": 31, 
    #     "SpD": 31, 
    #     "Spe": 31
    # }
    # moveset = [None, None, None, None]
    
    # find a way to scrape data from pokepaste
    pkm = pokemon()
    pkm.set_name()
    pkm.set_item()
    pkm.set_ability()
    pkm.set_tera()
    pkm.set_ev()
    pkm.set_nature()
    pkm.set_iv()
    pkm.set_moveset()
    

def parse_all_pokepastes():
    for paste in pokepastes:
        driver.get(paste)
        parse_pokepaste()


def main():
    open_webpage()
    get_pokepaste_links()
    parse_all_pokepastes()
    driver.quit()

main()