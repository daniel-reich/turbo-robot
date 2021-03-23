"""


Four friends are playing a simple dice game (players are denoted p1, p2, p3
and p4). In each round, all players roll a pair of six-sided dice. The player
with the lowest total score is removed. If the lowest score is shared by two
or more players, the player in that group with the lowest score from their
_first_ dice is removed. If the lowest score is still shared (i.e. two or more
players have the same rolls in the same order), then _all_ players roll again.
This process continues until one player remains. Given a list of scores only
(given in player order for each round), return the winning player.

### Example

    dice_game([(6, 2), (4, 3), (3, 4), (5, 4), (3, 5), (1, 5), (4, 3), (1, 5), (1, 5), (5, 6), (2, 2)]) ➞ "p1"
    
                 p1      p2      p3      p4
    Round 1 -> (6, 2), (4, 3), (3, 4), (5, 4)  Player 3 removed.
    Round 2 -> (3, 5), (1, 5),         (4, 3)  Player 2 removed.
    Round 3 -> (1, 5),                 (1, 5)  No lowest score, players roll again.
    Round 4 -> (5, 6),                 (2, 2)  Player 1 wins!

### Notes

N/A

"""

def dice_game(scores):
​
  class Player:
​
    def __init__(self, name,  alive = True, scores = [], winner = False):
      self.n = name
      self.a = alive
      self.s = scores
      self.w = winner
    
    def kill(self):
      self.a = False
      return True
    
    def add_score(self, score):
      self.s.append(score)
      return self.s
  
  class Game:
​
    def __init__(self, players, raw_scores, winner = None):
      self.p = players
      self.rs = raw_scores
      self.w = winner
      self.pn = len(players)
    
    def rnd(self):
      rnd_scores = []
      rnd_tuples = []
      for n in range(0, self.pn):
        score = sum(list(self.rs[0]))
        rnd_scores.append(score)
        rnd_tuples.append(self.rs[0])
        self.rs.pop(0)
      
      r_players = []
      
      for player in self.p:
        if player.a == True:
          r_players.append(player)
      
      player_scores = {}
      for n in range(0, len(r_players)):
        player = r_players[n]
        score = rnd_scores[n]
​
        if score not in player_scores.keys():
          if rnd_scores.count(score) == 1:
            player_scores[score] = player
          else:
            player_scores[score] = [[player, rnd_tuples[n]]]
        else:
          player_scores[score].append([player, rnd_tuples[n]])
      
      to_kick = min(rnd_scores)
​
      t = rnd_scores.count(to_kick)
​
      if t == 1:
        return player_scores[to_kick]
      else:
        kickable = player_scores[to_kick]
        
        kick_tuples = {}
        imp_nums = []
​
        for lst in kickable:
          player = lst[0]
          tupl = lst[1]
​
          imp_num = int(tupl[0])
​
          imp_nums.append(imp_num)
          kick_tuples[imp_num] = player
        
        if imp_nums.count(min(imp_nums)) == 1:
          return kick_tuples[min(imp_nums)]
        else:
          return False
​
    def play(self):
​
      victor = None
      c = 0
      
      while self.pn > 1 and c != 1000:
        r = self.rnd()
        if r != False:
          r.kill()
          for n in range(self.pn):
            try:
              player = self.p[n]
            except IndexError:
              return self.p, self.pn, c
            if player.a == False:
              self.p.pop(n)
              break
          
          self.pn -= 1
        c += 1
        
      
      winner = self.p[0].n
      self.w = winner
      return winner
​
  p1 = Player('p1')
  p2 = Player('p2')
  p3 = Player('p3')
  p4 = Player('p4')
​
  g1 = Game([p1, p2, p3, p4], scores)
​
  
  t = g1.play()
​
  return t

