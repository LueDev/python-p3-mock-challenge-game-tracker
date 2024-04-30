from collections import defaultdict
from email.policy import default


class Game:
    def __init__(self, title) -> object:
        self.title = title
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else: 
            return ValueError("Already initialized or incorrect value inserted.")

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([result.player for result in Result.all if result.game == self]))

    def average_score(self, player):
        scores = [result.score for result in Result.all if result.player == player]
        if scores:
            return sum(scores) / len(scores)
        else:
            return 0
    
    def __str__(self):
        return f"Game STR: {self.title}"
    
    def __repr__(self):
        return self.title
    

class Player:
    all = set()
    
    def __init__(self, username):
        self.username = username
        Player.appendPlayer(self)
        
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username,str) and 1 < len(username) < 17: 
            self._username = username
        else: 
            return ValueError("The conditions are incorrect.")

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        games_played = list(set([result.game for result in Result.all if result.player == self]))
        return games_played

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return [result.game for result in Result.all if result.player == self].count(game)

    def __str__(self):
        return f"Player: {self.username}"
    
    @classmethod
    def appendPlayer(cls, player):
        cls.all.add(player)
    
    @classmethod
    def highest_scored(cls, game):
        if isinstance(game, Game):
            scores = {}
            for player in cls.all:
                scores[player] = game.average_score(player)
            return max(scores, key=scores.get)
        else:
            raise ValueError("Input should be an instance of Game.")

class Result:
    
    all = []
    
    def __init__(self, player, game, score):   
        self.player = player
        self.game = game
        self._score_initialized = False
        self.score = score
        Result.appendInstance(self)
      
    @classmethod 
    def appendInstance(cls, instance):
        cls.all.append(instance)
      
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if not self._score_initialized:
            if isinstance(score, int) and 1 <= score <= 5000:
                self._score = score 
                self._score_initialized = True
        else: 
           return
           
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        
    def __str__(self):
        return f"Result for Player: {self.player},  Game: {self.game}, Score: {self.score} "

    
if __name__ == "__main__":
    
    game = Game("Skribbl.io")
    player = Player("Nick")
    result_1 = Result(player, game, 2000)
    print(isinstance(result_1.score, int))
    result_1.score = 5000
    assert result_1.score == 2000
    assert isinstance(result_1.score, int)

