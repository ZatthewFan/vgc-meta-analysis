import math
import json

f = open("nature-val.json")
NATURE_VAL = json.load(f)
f = open("defense-type-chart.json")
DEFENSE_CHART = json.load(f)
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
    
    weaknesses = None
    
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
        
        self.weaknesses = {
            "normal": 1,
            "fire": 1,
            "water": 1,
            "electric": 1,
            "grass": 1,
            "ice": 1,
            "fighting": 1,
            "poison": 1,
            "ground": 1,
            "flying": 1,
            "psychic": 1,
            "bug": 1,
            "rock": 1,
            "ghost": 1,
            "dragon": 1,
            "dark": 1,
            "steel": 1,
            "fairy": 1
        }
    
    def set_name(self, name: str) -> None:
        self.name = name
    
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
    
    def set_nature(self, nature: str) -> None:
        self.nature = nature
    
    def set_iv(self, **kwargs: list[str | int]) -> None:
        for key, value in kwargs.items():
            self.iv[key] = value
    
    def set_moveset(self, moveset: list[str]) -> None:
        for slot in range(len(moveset)):
            self.moveset[slot] = moveset[slot]
    
    def set_dex_info(self, dex: dict) -> None:
        self.dex_info = dex
        self.set_type()
        self.set_base_stats()
        self.set_weaknesses()
    
    def set_type(self) -> None:
        types = [x.lower() for x in self.dex_info["types"]]
        self.pkm_type = types
    
    def set_base_stats(self) -> None:
        self.base_stats = self.dex_info["baseStats"]
        print(self.base_stats)
    
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
                total_stats[key] = math.floor((partial_stat + 5) * NATURE_VAL[self.nature.lower()][key])
        
        self.total_stats = total_stats
    
    def set_weaknesses(self) -> None:
        for my_type in self.pkm_type:
            for type in self.weaknesses.keys():
                self.weaknesses[type] *= DEFENSE_CHART[my_type][type]
    
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

    def get_weaknesses(self) -> dict[str, int]:
        return self.weaknesses