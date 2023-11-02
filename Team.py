from Pokemon import Pokemon
class Team:
    format = None
    teamlist = []
    is_ots = False
    
    def __init__(self, format: str) -> None:
        self.format = format
        self.teamlist = []
    
    def add_pkm(self, pkm: Pokemon) -> None:
        self.teamlist.append(pkm)
        
    def set_format(self, format: str) -> None:
        self.format = format
    
    def set_teamlist(self, teamlist: list[Pokemon]) -> None:
        self.teamlist = teamlist
        
    def set_ots(self, bool: bool) -> None:
        self.is_ots = bool
    
    def get_format(self) -> str:
        return self.format
    
    def get_teamlist(self) -> list[Pokemon]:
        return self.teamlist
    
    def get_ots(self) -> bool:
        return self.is_ots