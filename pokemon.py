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
    
    def set_ev(self, hp, atk, _def, spa, spd, spe):
        self.ev["HP"] = hp
        self.ev["Atk"] = atk
        self.ev["Def"] = _def
        self.ev["SpA"] = spa
        self.ev["SpD"] = spd
        self.ev["Spe"] = spe
    
    def set_nature(self, nature):
        self.nature = nature
    
    def set_iv(self, hp, atk, _def, spa, spd, spe):
        self.iv["HP"] = hp
        self.iv["Atk"] = atk
        self.iv["Def"] = _def
        self.iv["SpA"] = spa
        self.iv["SpD"] = spd
        self.iv["Spe"] = spe
    
    def set_moveset(self, slot0, slot1, slot2, slot3):
        self.moveset[0] = slot0
        self.moveset[1] = slot1
        self.moveset[2] = slot2
        self.moveset[3] = slot3