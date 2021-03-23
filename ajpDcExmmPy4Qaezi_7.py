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

def EPLResult(table, team):
  x = table[:]
  newlist = []
  goal_diff_dict = {}
  points_amount = {}
  positions = {1: '1st', 2: '2nd', 3: '3rd', 4: '4th', 5: '5th', 6: '6th', 7: '7th', 8: '8th', 9: '9th', 10: '10th', 11: '11th', 12: '12th', 13: '13th', 14: '14th', 15: '15th', 16: '16th', 17: '17th', 18: '18th', 19: '19th', 20: '20th', 21: '21st', 22: '22nd'}
  for eachteam in x:
    total_points = 0
    goal_diff_dict[eachteam[0]] = eachteam[-1]
    total_points += eachteam[2]*3 + eachteam[3]
    newlist.append([eachteam[0],total_points])
  z = sorted(newlist, key = get_points)[::-1]
  for x,y in z:
    points_amount[x] = y
  newlist3 = []
  team_points = 0
  behind_them = 0
  curr_team = []
  for eachteam in z:
    if eachteam[0] == team:
      newlist3.append(eachteam)
      team_points = eachteam[1]
      curr_team = eachteam
      break
  for eachteam in z:
    if eachteam[0] != team and eachteam[1] == team_points:
      newlist3.append(eachteam)
  if len(newlist3) == 1:
    return '{} came {} with {} points and a goal difference of {}!'.format(newlist3[0][0],positions[z.index(newlist3[0])+1],newlist3[0][1],goal_diff_dict[newlist3[0][0]])
  else:
    curr_team_diff = goal_diff_dict[team]
    curr_team_points = points_amount[team]
    for eachteam in newlist3:
      if goal_diff_dict[eachteam[0]] > curr_team_diff:
        behind_them += 1
      elif goal_diff_dict[eachteam[0]] < curr_team_diff and z.index(eachteam) < z.index(curr_team):
        behind_them -= 1
    return '{} came {} with {} points and a goal difference of {}!'.format(newlist3[0][0],positions[z.index(newlist3[0])+1+behind_them],newlist3[0][1],goal_diff_dict[newlist3[0][0]])
    
  
  
def get_points(eachteam):
  return eachteam[1]

