from fetch_and_parse import FetchFromURL

def name_test(team, expected):
    result = []
    for pkm in team:
        result.append(pkm.get_name())
    
    assert result == expected

def item_test(team, expected):
    result = []
    for pkm in team:
        result.append(pkm.get_item())
    
    assert result == expected

def ability_test(team, expected):
    result = []
    for pkm in team:
        result.append(pkm.get_ability())
    
    assert result == expected

def level_test(team, expected):
    result = []
    for pkm in team:
        result.append(pkm.get_level())

def tera_test(team, expected):
    result = []
    for pkm in team:
        result.append(pkm.get_tera())
    
    assert result == expected

def ev_test(team, expected):
    # flutter mane
    result = team.get_teamlist()[1].get_ev()
    
    assert result == expected

def nature_test(team, expected):
    result = []
    for pkm in team:
        result.append(pkm.get_nature())
    
    assert result == expected

def iv_test(team, expected):
    # lando-t
    result = team.get_teamlist()[2].get_iv()
    
    assert result == expected

def moveset_test(team, expected):
    # ogerpon
    result = team.get_teamlist()[4].get_moveset()
    
    assert result == expected

def type_test(team, expected):
    # ogerpon
    result = team.get_teamlist()[4].get_type()
    
    assert result == expected

def base_stat_test(team, expected):
    # rillaboom
    result = team.get_teamlist()[3].get_base_stats()
    
    assert result == expected

def total_stat_test(team, expected):
    # flutter mane
    result = team.get_teamlist()[1].get_total_stats()
    print(f"result: {result}")
    
    assert result == expected


if __name__ == "__main__":
    fetched = FetchFromURL("https://pokepast.es/22b07255f896b829", "gen9vgc2023regulatione")
    fetched.open_webpage()
    test_team = fetched.parse_pokepaste()
    
    name_test(test_team, ["Tornadus", "Flutter Mane", "Landorus-Therian", "Rillaboom", "Ogerpon-Hearthflame (F)", "Farigiraf"])
    item_test(test_team, ["Focus Sash", "Booster Energy", "Choice Scarf", "Assault Vest", "Hearthflame Mask", "Rocky Helmet"])
    ability_test(test_team, ["Prankster", "Protosynthesis", "Intimidate", "Grassy Surge", "Mold Breaker", "Armor Tail"])
    level_test(test_team, [50, 50, 50, 50, 50, 50])
    tera_test(test_team, ["Ghost", "Fairy", "Flying", "Fire", "Fire", "Fairy"])
    ev_test(test_team, {"hp": 76, "atk": 0, "def": 100, "spa": 116, "spd": 4, "spe": 212}) # only flutter mane
    nature_test(test_team, ["Timid", "Modest", "Adamant", "Adamant", "Jolly", "Bold"])
    iv_test(test_team, {"hp": 31, "atk": 31, "def": 31, "spa": 31, "spd": 31, "spe": 31}) # only lando-t
    moveset_test(test_team, ["Ivy Cudgel", "Grassy Glide", "Stomping Tantrum", "Spiky Shield"]) # only ogerpon
    type_test(test_team, ["grass", "fire"]) # only ogerpon
    base_stat_test(test_team, {"hp": 100, "atk": 125, "def": 90, "spa": 60, "spd": 70, "spe": 85}) # only rillaboom
    total_stat_test(test_team, {"hp": 140, "atk": 54, "def": 88, "spa": 187, "spd": 156, "spe": 182})
    
    print(test_team)