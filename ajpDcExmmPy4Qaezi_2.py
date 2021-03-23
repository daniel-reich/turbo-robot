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
  t=sorted(table, key=lambda x: (x[2]*3+x[3], x[-1]), reverse=True)
  p=[x+[t.index(x)] for x in t]
  d={x[0]:x[1:] for x in p}
  pts=d[team][1]*3+d[team][2]
  ordinal=lambda i: '{}'.format('tsnrhtdd'[(i//10%10!=1)*(i%10<4)*i%10::4])
  rank='{}{}'.format(d[team][-1]+1, ordinal(d[team][-1]+1))
  gd=d[team][-2]
  res="{} came {} with {} points and a goal difference of {}!".format(team, rank, pts, gd)
  return res

