class Team:
    vgc_format = None
    teamlist = []
    
    def __init__(self, format):
        self.format = format
        self.teamlist = []
    
    def add_pkm(self, pkm):
        self.teamlist.append(pkm)