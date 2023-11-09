from fetch_and_parse import FetchFromURL




if __name__ == "__main__":
    test_team = FetchFromURL("https://pokepast.es/22b07255f896b829", "gen9vgc2023regulatione")
    test_team.open_webpage()
    team = test_team.parse_pokepaste()
    
    for pkm in team:
        print(pkm.get_name())