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
    
    
    
    
    def set_name(self, name):
        self.name = name
    
    def set_item(self, item):
        self.item = item
    
    def set_ability(self, ability):
        self.ability = ability
    
    def set_tera(self, tera):
        self.tera = tera
    
    def set_ev(self, **kwargs):
        for key, value in kwargs.items():
            self.ev[key] = value
    
    def set_nature(self, nature):
        self.nature = nature
    
    def set_iv(self, **kwargs):
        for key, value in kwargs.items():
            self.iv[key] = value
    
    def set_moveset(self, moveset):
        self.moveset[0] = moveset[0]
        self.moveset[1] = moveset[1]
        self.moveset[2] = moveset[2]
        self.moveset[3] = moveset[3]
    
    def get_name(self):
        return self.name
    
    def get_item(self):
        return self.item
    
    def get_ability(self):
        return self.ability
    
    def get_tera(self):
        return self.tera
    
    def get_ev(self):
        return self.ev
    
    def get_nature(self):
        return self.nature
    
    def get_iv(self):
        return self.iv
    
    def get_moveset(self):
        return self.moveset