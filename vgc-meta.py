from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://victoryroadvgc.com/sv-rental-teams-2023/"

options = webdriver.ChromeOptions()
options.add_argument("load-extension=./ublock-1.52.2_1")
driver = webdriver.Chrome(options=options)

pokepastes = []

def open_webpage():
    driver.get(BASE_URL)

def get_pokepaste_links():
    pokepaste_links = driver.find_elements(By.XPATH, '//a[contains(@href, "pokepast.es")]')
    for link in pokepaste_links:
        pokepastes.append(link.get_attribute('href'))
    
def open_all_pokepastes():
    for paste in pokepastes:
        driver.get(paste)


def main():
    open_webpage()
    get_pokepaste_links()
    open_all_pokepastes()
    driver.quit()

main()