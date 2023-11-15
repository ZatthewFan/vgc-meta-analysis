from fetch_and_parse import FetchFromURL
from modules.pokemon import Pokemon

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
    
    assert result == expected

def tera_test(team, expected):
    result = []
    for pkm in team:
        result.append(pkm.get_tera())
    
    assert result == expected

def ev_test(pkm, expected):
    result = pkm.get_ev()
    
    assert result == expected

def nature_test(team, expected):
    result = []
    for pkm in team:
        result.append(pkm.get_nature())
    
    assert result == expected

def iv_test(pkm, expected):
    result = pkm.get_iv()
    
    assert result == expected

def moveset_test(pkm, expected):
    result = pkm.get_moveset()
    
    assert result == expected

def type_test(pkm, expected):
    result = pkm.get_type()
    
    assert result == expected

def base_stat_test(pkm, expected):
    result = pkm.get_base_stats()
    
    assert result == expected

def total_stat_test(pkm, expected):
    result = pkm.get_total_stats()
    
    assert result == expected

def weakness_test(pkm, expected):
    result = pkm.get_weaknesses()
    
    assert result == expected

if __name__ == "__main__":
    fetched = FetchFromURL("https://pokepast.es/22b07255f896b829", "gen9vgc2023regulatione")
    fetched.open_webpage()
    test_team = fetched.parse_pokepaste()
    
    name_test(test_team, ["Tornadus", "Flutter Mane", "Landorus-Therian", "Rillaboom", "Ogerpon-Hearthflame", "Farigiraf"])
    
    item_test(test_team, ["Focus Sash", "Booster Energy", "Choice Scarf", "Assault Vest", "Hearthflame Mask", "Rocky Helmet"])
    
    ability_test(test_team, ["Prankster", "Protosynthesis", "Intimidate", "Grassy Surge", "Mold Breaker", "Armor Tail"])
    
    level_test(test_team, [50, 50, 50, 50, 50, 50])
    
    tera_test(test_team, ["Ghost", "Fairy", "Flying", "Fire", "Fire", "Fairy"])
    
    ev_test(test_team.get_teamlist()[1], {"hp": 76, "atk": 0, "def": 100, "spa": 116, "spd": 4, "spe": 212}) # only flutter mane
    
    nature_test(test_team, ["Timid", "Modest", "Adamant", "Adamant", "Jolly", "Bold"])
    
    iv_test(test_team.get_teamlist()[2], {"hp": 31, "atk": 31, "def": 31, "spa": 31, "spd": 31, "spe": 31}) # only lando-t
    
    moveset_test(test_team.get_teamlist()[4], ["Ivy Cudgel", "Grassy Glide", "Stomping Tantrum", "Spiky Shield"]) # only ogerpon
    
    type_test(test_team.get_teamlist()[4], ["grass", "fire"]) # only ogerpon
    
    base_stat_test(test_team.get_teamlist()[3], {"hp": 100, "atk": 125, "def": 90, "spa": 60, "spd": 70, "spe": 85}) # only rillaboom
    
    total_stat_test(test_team.get_teamlist()[1], {"hp": 140, "atk": 54, "def": 88, "spa": 187, "spd": 156, "spe": 182}) # only flutter mane
    
    weakness_test(test_team.get_teamlist()[4], {
        "normal": 1,
        "fire": 1,
        "water": 1,
        "electric": 0.5,
        "grass": 0.25,
        "ice": 1,
        "fighting": 1,
        "poison": 2,
        "ground": 1,
        "flying": 2,
        "psychic": 1,
        "bug": 1,
        "rock": 2,
        "ghost": 1,
        "dragon": 1,
        "dark": 1,
        "steel": 0.5,
        "fairy": 0.5
    })
    
    print(test_team)