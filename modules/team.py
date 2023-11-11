from modules.pokemon import Pokemon
class Team:
    format = None
    teamlist = None
    is_ots = None
    iter_count = None
    
    def __init__(self, format: str) -> None:
        self.format = format
        self.teamlist = []
        self.is_ots = True
        self.iter_count = None
    
    def __iter__(self):
        self.iter_count = 0
        return self
    
    def __next__(self):
        if self.iter_count < len(self.teamlist):
            pkm = self.teamlist[self.iter_count]
            self.iter_count += 1
            return pkm
        else:
            raise StopIteration
    
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