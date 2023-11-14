import requests
import math
import json

f = open("nature-val.json")
NATURE_VAL = json.load(f)
class Pokemon:
    name = None
    item = None
    ability = None
    level = None
    tera = None
    ev = None
    nature = None
    iv = None
    moveset = None
    
    dex_info = None
    
    pkm_type = None
    base_stats = None
    total_stats = None
    
    # # TODO add weaknesses and resistance chart
    # weaknesses = {
    #     "normal": 1,
    #     "fighting": 1,
    #     "flying": 1,
    #     "poison": 1,
    #     "ground": 1,
    #     "rock": 1,
    #     "bug": 1,
    #     "ghost": 1,
    #     "steel": 1,
    #     "fire": 1,
    #     "water": 1,
    #     "grass": 1,
    #     "electric": 1,
    #     "psychic": 1,
    #     "ice": 1,
    #     "dragon": 1,
    #     "dark": 1,
    #     "fairy": 1
    # }
    
    # # pokemondb's ordering
    # weaknesses = {
    #     "normal": 1,
    #     "fire": 1,
    #     "water": 1,
    #     "electric": 1,
    #     "grass": 1,
    #     "ice": 1,
    #     "fighting": 1,
    #     "poison": 1,
    #     "ground": 1,
    #     "flying": 1,
    #     "psychic": 1,
    #     "bug": 1,
    #     "rock": 1,
    #     "ghost": 1,
    #     "dragon": 1,
    #     "dark": 1,
    #     "steel": 1,
    #     "fairy": 1
    # }
    
    def __init__(self):
        self.name = None
        self.item = None
        self.ability = None
        self.level = None
        self.tera = None
        self.ev = {
            "hp" : 0, 
            "atk": 0, 
            "def": 0, 
            "spa": 0, 
            "spd": 0, 
            "spe": 0
        }
        self.nature = None
        self.iv = {
            "hp" : 31, 
            "atk": 31, 
            "def": 31, 
            "spa": 31, 
            "spd": 31, 
            "spe": 31
        }
        self.moveset = [None, None, None, None]
        
        self.dex_info = None
        
        self.pkm_type = None
        self.base_stats = None
        self.total_stats = None
    
    def set_name(self, name: str) -> None:
        self.name = name
        
        self.get_dex_info(self.name)
        
        self.set_type()
        self.set_base_stats()
    
    def set_item(self, item: str) -> None:
        self.item = item
    
    def set_ability(self, ability: str) -> None:
        self.ability = ability
    
    def set_level(self, level: int) -> None:
        self.level = level
    
    def set_tera(self, tera: str) -> None:
        self.tera = tera
    
    def set_ev(self, **kwargs: list[str | int]) -> None:
        for key, value in kwargs.items():
            self.ev[key] = value
        
        # set the total stats
        self.set_total_stats()
    
    def set_nature(self, nature: str) -> None:
        self.nature = nature
    
    def set_iv(self, **kwargs: list[str | int]) -> None:
        for key, value in kwargs.items():
            self.iv[key] = value
    
    def set_moveset(self, moveset: list[str]) -> None:
        for slot in range(len(moveset)):
            self.moveset[slot] = moveset[slot]
            
    def get_dex_info(self, pkm_name: str) -> None:
        base_url = f"https://play.pokemonshowdown.com/data/pokedex.json"
        response = requests.get(base_url)
        
        if response.status_code != 200:
            print(f"error: {response.status_code}")

        # keys are all lowercase, no spaces, no forme hyphens, and no gender indication outside of formes
        # (for example: Ogerpon-Hearthflame (F) --> ogerponhearthflame)
        dex_key = pkm_name.lower().replace(" ", "").replace("-", "").split("(")[0]
        self.dex_info = response.json()[dex_key]
    
    def set_type(self) -> None:
        types = [x.lower() for x in self.dex_info["types"]]
        self.pkm_type = types
    
    def set_base_stats(self) -> None:
        self.base_stats = self.dex_info["baseStats"]
    
    def set_total_stats(self) -> None:
        # formulas are from https://bulbapedia.bulbagarden.net/wiki/Stat#Generation_III_onward
        total_stats = {
            "hp": 0,
            "atk": 0,
            "def": 0,
            "spa": 0,
            "spd": 0,
            "spe": 0
        }
        
        for key in total_stats.keys():
            partial_stat = math.floor(
                (((2*self.base_stats[key]) + (self.iv[key]) + math.floor(self.ev[key]/4)) * self.level) / 100
            )
            if key == "hp":
                if self.name == "Shedinja":
                    total_stats[key] = 1
                else:
                    total_stats[key] = partial_stat + self.level + 10
            else:
                # total_stats[key] = math.floor((partial_stat + 5) * NATURE_VAL[self.nature.lower()])
                print("not reached nature")
        
        self.total_stats = total_stats
    
    def get_name(self) -> str:
        return self.name
    
    def get_item(self) -> str:
        return self.item
    
    def get_ability(self) -> str:
        return self.ability
    
    def get_level(self) -> int:
        return self.level
    
    def get_tera(self) -> str:
        return self.tera
    
    def get_ev(self) -> dict[str, int]:
        return self.ev
    
    def get_nature(self) -> str:
        return self.nature
    
    def get_iv(self) -> dict[str, int]:
        return self.iv
    
    def get_moveset(self) -> list[str]:
        return self.moveset
    
    def get_type(self) -> list[str]:
        return self.pkm_type
    
    def get_base_stats(self) -> dict[str, int]:
        return self.base_stats
    
    def get_total_stats(self) -> dict[str, int]:
        return self.total_stats