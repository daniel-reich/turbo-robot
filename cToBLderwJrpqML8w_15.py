"""


Create a function that takes a list of football clubs with properties: `name,
wins, loss, draws, scored, conceded`, and returns the **team name** with the
highest number of points. If two teams have the **same number of points** ,
return the team with the **largest goal difference**.

### How to Calculate Points and Goal Difference

    team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88, "conceded": 20 }
    
    Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
    Goal Difference = scored - conceded = 88 - 20 = 68

### Examples

    champions([
      {
        "name": "Manchester United",
        "wins": 30,
        "loss": 3,
        "draws": 5,
        "scored": 88,
        "conceded": 20,
      },
      {
        "name": "Arsenal",
        "wins": 24,
        "loss": 6,
        "draws": 8,
        "scored": 98,
        "conceded": 29,
      },
      {
        "name": "Chelsea",
        "wins": 22,
        "loss": 8,
        "draws": 8,
        "scored": 98,
        "conceded": 29,
      }
    ]) ➞ "Manchester United"

### Notes

Input is a list of teams.

"""

def champions(t):
  a=[[t[i]['name'],t[i]['wins']*3+t[i]['draws'],t[i]['scored']-t[i]['conceded']] for i in range(3)]
  b=[a[i][1] for i in range(3)]
  c=[a[i][2] for i in range(3)]
  d=[]
  e=[]
​
  for i in range(len(a)):
    if a[i][1]==max(b):
      d.append(a[i])
  if len(d)==1:
    return d[0][0]
​
  c=[d[i][2] for i in range(2)]
​
  if len(d)>1:
    print(d)
    for i in range(len(d)):
      if d[i][2]==max(c):
        e.append(d[i])  
    return e[0][0]

