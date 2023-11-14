from modules.pokemon import Pokemon
from fetch_and_parse import FetchFromURL
import re

def parse_ev_iv(which: str, pkm: Pokemon, stats: list[str]) -> None:
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

def parse_mon(pkm, pkm_set) -> Pokemon:
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
            pkm.set_level(line.split(":")[1].strip())
        elif "Tera Type" in line:
            pkm.set_tera(line.split(":")[1].strip())
        elif "EVs" in line:
            parse_ev_iv("ev", pkm, re.split(": | / ", line)[1:])
            # team.set_ots(False)
        elif "Nature" in line:
            pkm.set_nature(line.split()[0].strip())
        elif "IVs" in line:
            parse_ev_iv("iv", pkm, re.split(": | / ", line)[1:])
    
    # last 4 lines are probably the moves
    # parse_moveset(pkm, pkm_set[-4:])
    
    return pkm

if __name__ == "__main__":
    test_pkm = Pokemon()
    
    test_pkm = parse_mon(test_pkm, [
        "Landorus-Therian @ Choice Scarf  ", 
        "Ability: Intimidate  ", 
        "Level: 50 ", 
        "Tera Type: Flying ", 
        "EVs: 60 HP / 196 Atk / 252 Spe", 
        "Adamant Nature ", 
        "- Stomping Tantrum ", 
        "- Tera Blast ", 
        "- Rock Slide ", 
        "- U-turn "])
    
    print(test_pkm.get_ev())
    print(test_pkm.get_iv())
    print(test_pkm.get_level())