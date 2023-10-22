class Team:
    format = None
    teamlist = []
    is_ots = False
    
    def __init__(self, format):
        self.format = format
        self.teamlist = []
    
    def add_pkm(self, pkm):
        self.teamlist.append(pkm)
        
    def set_format(self, format):
        self.format = format
    
    def set_teamlist(self, teamlist):
        self.teamlist = teamlist
        
    def set_ots(self, bool):
        self.is_ots = bool
    
    def get_format(self):
        return self.format
    
    def get_teamlist(self):
        return self.teamlist
    
    def get_ots(self):
        return self.is_ots