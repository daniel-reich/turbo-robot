"""


The 2019/20 season of the English Premier League (EPL) saw Liverpool FC win
the title for the first time despite their bitter rivals, Manchester United,
having won 13 titles!

Create a function that receives an alphabetically sorted array of the results
achieved by each team in that season and the name of one of the teams. The
function should return a string giving the final position of the team, the
number of points achieved and the goal difference (see examples for precise
format).

The results table is given in the following format:

Team| Played| Won| Drawn| Lost| G/Diff  
---|---|---|---|---|---  
Arsenal| 38| 14| 14| 10| 8  
Aston Villa| 38| 9| 8| 21| -26  
Bournemouth| 38| 9| 7| 22| -26  
Brighton| 38| 9| 14| 15| -15  
Burnley| 38| 15| 9| 14| -7  
Chelsea| 38| 20| 6| 12| 15  
Crystal Palace| 38| 11| 10| 17| -19  
Everton| 38| 13| 10| 15| -12  
Leicester City| 38| 18| 8| 12| 26  
Liverpool| 38| 32| 3| 3| 52  
Manchester City| 38| 26| 3| 9| 67  
Manchester Utd| 38| 18| 12| 8| 30  
Newcastle| 38| 11| 11| 16| -20  
Norwich| 38| 5| 6| 27| -49  
Sheffield Utd| 38| 14| 12| 12| 0  
Southampton| 38| 15| 7| 16| -9  
Tottenham| 38| 16| 11| 11| 14  
Watford| 38| 8| 10| 20| -28  
West Ham| 38| 10| 9| 19| -13  
Wolves| 38| 15| 14| 9| 11  
  
### Examples

    table = [
      ["Arsenal", 38, 14, 14, 10, 8],
      ["Aston Villa", 38, 9, 8, 21, -26],
      ...
      ...
      ["West Ham", 38, 10, 9, 19, -13],
      ["Wolves", 38, 15, 14, 9, 11]
    ]
    
    EPLResult(table, "Liverpool")
      ➞ "Liverpool came 1st with 99 points and a goal difference of 52!"
    
    EPLResult(table, "Manchester Utd")
      ➞ "Manchester Utd came 3rd with 66 points and a goal difference of 30!"
    
    EPLResult(table, "Norwich")
      ➞ "Norwich came 22nd with 21 points and a goal difference of -49!"

### Notes

  * Score 3 points for a win and 1 point for a draw.
  * If teams are tied on points, their position is determined by better goal difference.
  * The input table should be considered immutable - do not make any changes to it!

"""

class League:
  class Team:
​
    def __init__(self, name, played, won, drawn, lost, g_diff):
      self.name = name
      self.play = played
      self.won = won
      self.draw = drawn
      self.lost = lost
      self.gdif = g_diff
​
      self.points = (self.won * 3) + self.draw
    
    def __lt__(self, other):
​
      if self.points != other.points:
        return self.points < other.points
      else:
        return self.gdif < other.gdif
    
    def __gt__(self, other):
      if self.points != other.points:
        return self.points > other.points
      else:
        return self.gdif > other.gdif
    
    def data(self):
      return [self.name, self.points, self.gdif]
  
  def __init__(self, league):
​
    self.l = league
    self.teams = {}
​
    for lst in league:
      name, games, won, drawn, lost, gd = lst
      team = League.Team(name, games, won, drawn, lost, gd)
      self.teams[name] = team
  
  def find_winner(teams, tid):
    team = teams[tid]
    for ti in teams.keys():
      if ti != tid:
        if team < teams[ti]:
          return League.find_winner(teams, ti)
    return tid
  
  def find_loser(teams, tid):
    try:
      team = teams[tid]
    except TypeError:
      print(teams, tid)
      return 'hjlks'
    for ti in teams.keys():
      if ti != tid:
        if team > teams[ti]:
          return League.find_loser(teams, ti)
    return tid
  
  def sort_teams(dict, teams):
    if len(teams) == 0:
      return []
    elif len(teams) == 1:
      return [teams[0]]
    else:
     # print(teams)
      loser = League.find_loser(dict, teams[0])
      winner = League.find_winner(dict, teams[0])
      try:
        teams.pop(teams.index(loser))
        teams.pop(teams.index(winner))
        nd = {key: dict[key] for key in dict.keys() if key not in [loser, winner]}
      except ValueError:
        print('Loser: {}\nWinner: {}\nTeams: {}'.format(loser, winner, teams),'Norwich' in teams)
        return []
      return [loser] + League.sort_teams(nd, teams) + [winner]
​
  def find_team_place(self, team):
    sorted_teams = League.sort_teams(self.teams, list(self.teams.keys()))
    
    place = 1
​
    while sorted_teams[-place] != team:
      #print(place)
      place += 1
    
    return place
​
def EPLResult(table, team):
​
  league = League(table)
​
  poss = league.find_team_place(team)
  exceptions = {1: '1st', 2: '2nd', 3: '3rd'}
​
  if poss in exceptions.keys():
    pos = exceptions[poss]
  else:
    pos = '{}th'.format(poss)
​
  Team = league.teams[team]
​
  return "{} came {} with {} points and a goal difference of {}!".format(Team.name, pos, Team.points, Team.gdif)

