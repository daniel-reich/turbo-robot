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

def champions(teams):
    lst=[]
    c=0
    while c < len(teams):
        points=0
        score=0
        points+=teams[c]["wins"]*3
        points+=teams[c]["draws"]*1
        score+=teams[c]["scored"]-teams[c]["conceded"]
        lst.append([teams[c]["name"],points,score])
        c+=1
    points=0
    score=0
    winner=""
    wc=0
    res=[]
    for i in range(0, len(lst)):
        if lst[i][1] > points:
            points=lst[i][1]
            res=[lst[i]]
            wc+=1
        elif lst[i][1] == points:
            res.append(lst[i])
    if wc==1:
        return res[0][0]
    else:
        for i in range(0,len(res)):
            if res[i][2] > score:
                score=res[i][2]
                winner=res[i][0]
            else:
                pass
        return winner

