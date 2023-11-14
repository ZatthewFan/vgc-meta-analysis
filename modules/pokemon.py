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
    
    pkm_type = None
    base_stats = None
    total_stats = None
    # TODO add weaknesses and resistance chart
    
    def __init__(self):
        self.name = None
        self.item = None
        self.ability = None
        self.level = None
        self.tera = None
        self.ev = {
            "HP" : 0, 
            "Atk": 0, 
            "Def": 0, 
            "SpA": 0, 
            "SpD": 0, 
            "Spe": 0
        }
        self.nature = None
        self.iv = {
            "HP" : 31, 
            "Atk": 31, 
            "Def": 31, 
            "SpA": 31, 
            "SpD": 31, 
            "Spe": 31
        }
        self.moveset = [None, None, None, None]
        
        self.pkm_type = None
        self.base_stats = None
        self.total_stats = None
    
    
    def set_name(self, name: str) -> None:
        self.name = name
        
        self.pkm_type = self.set_type(self.name)
        self.base_stats = self.set_base_stats(self.name)
    
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
    
    def set_nature(self, nature: str) -> None:
        self.nature = nature
    
    def set_iv(self, **kwargs: list[str | int]) -> None:
        for key, value in kwargs.items():
            self.iv[key] = value
    
    def set_moveset(self, moveset: list[str]) -> None:
        # self.moveset[0] = moveset[0]
        # self.moveset[1] = moveset[1]
        # self.moveset[2] = moveset[2]
        # self.moveset[3] = moveset[3]
        for slot in moveset:
            self.moveset[slot] = moveset[slot]
    
    def set_type(self, pkm_name):
        self.pkm_type = None # TODO use api to get type
    
    def set_base_stats(self, pkm_name):
        self.base_stats = None # TODO use api to get base stats
    
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
    
    def get_type(self) -> tuple(str):
        return self.pkm_type
    
    def get_base_stats(self) -> dict[str, int]:
        return self.base_stats
    
    def get_total_stats(self) -> dict[str, int]:
        return self.total_stats