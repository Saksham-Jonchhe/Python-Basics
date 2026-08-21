class Player:
    def __init__(self,playername,playerrole,playerage):
        self.playername=playername
        self.playerrole=playerrole
        self.playerage=playerage
        print(f"\nPlayer created:{self.playername},{self.playerrole},{self.playerage}")


class Teams(Player):
    
    def __init__(self,team):
        self.teamname=team
        self.players=[]

    def add_players(self,*player):
            self.players.extend(player)
            
    
    def showteam(self):
        
        print(f"Team Name:{self.teamname}")
        print(f"PLayers: ")
        for player in self.players:
            print(f"{player.playername} - {player.playerrole} -{player.playerage}")

class Match:
    def __init__(self,*teamname):
        self.matches=[]
        self.teams=teamname

    def schedule(self):
        
        self.matches=self.teams

    def showmatches(self):
        print(f"{self.matches[0].teamname}vs{self.matches[1].teamname} ")
        # print(f"{self.matches[0].teamname}vs{self.matches[1].teamname} ")
        # print(f"{self.matches[0].teamname}vs{self.matches[1].teamname} ")
        print()