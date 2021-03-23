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
    z = list(zip(*[[team["name"],3*team["wins"]+team["draws"], team["scored"]-team["conceded"]] for team in teams]))
    m1_pos = [i for i, e in enumerate(z[1]) if e==max(z[1])]
    return z[0][z[1].index(max(z[1]))] if len(m1_pos)==1 else z[0][z[2].index(max(z[2][m1_pos[0]], z[2][m1_pos[1]]))]

