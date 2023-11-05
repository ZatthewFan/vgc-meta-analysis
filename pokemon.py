class Pokemon:
    name = None
    item = None
    ability = None
    tera = None
    ev = {
        "HP" : 0, 
        "Atk": 0, 
        "Def": 0, 
        "SpA": 0, 
        "SpD": 0, 
        "Spe": 0
    }
    nature = None
    iv = {
        "HP" : 31, 
        "Atk": 31, 
        "Def": 31, 
        "SpA": 31, 
        "SpD": 31, 
        "Spe": 31
    }
    moveset = [None, None, None, None]
    
    
    
    
    def set_name(self, name: str) -> None:
        self.name = name
    
    def set_item(self, item: str) -> None:
        self.item = item
    
    def set_ability(self, ability: str) -> None:
        self.ability = ability
    
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
        self.moveset[0] = moveset[0]
        self.moveset[1] = moveset[1]
        self.moveset[2] = moveset[2]
        self.moveset[3] = moveset[3]
    
    def get_name(self) -> str:
        return self.name
    
    def get_item(self) -> str:
        return self.item
    
    def get_ability(self) -> str:
        return self.ability
    
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