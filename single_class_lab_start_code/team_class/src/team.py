from pickle import FALSE


class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
        self.win_points = {
            True : 3,
            False : 0
        }

    def add_player(self, new_player):
        self.players.append(new_player)   

    def has_player(self, search_name):
        found = False
        for player in self.players:
            if player == search_name:
                found = True
                return found

        return found

    def play_game(self, win_status):
        self.points += self.win_points[win_status]
