"""


Given an array of users, each defined by an object with the following
properties: `name`, `score`, `reputation` create a function that sorts the
array to form the correct leaderboard.

The leaderboard takes into consideration the score of each user of course, but
an _emphasis_ is put on their `reputation` in the community, so to get the
`trueScore`, you should add the `reputation` multiplied by `2` to the `score`.

Once you know the `trueScore` of each user, sort the array according to it in
**descending order**.

### Examples

    leaderboards([
      { "name": "a", "score": 100, "reputation": 20 },
      { "name": "b", "score": 90, "reputation": 40 },
      { "name": "c", "score": 115, "reputation": 30 },
    ]) ➞ [
      { "name": "c", "score": 115, "reputation": 30 },  # trueScore = 175
      { "name": "b", "score": 90, "reputation": 40 },   # trueScore = 170
      { "name": "a", "score": 100, "reputation": 20 }   # trueScore = 140
    ]

### Notes

N/A

"""

def leaderboards(users):
  
  Names = []
  Scores = []
  Reputations = []
    
  Counter = 0
  Length = len(users)
    
  while (Counter < Length):
        
    Thing = users[Counter]
        
    Names.append(Thing["name"])
    Scores.append(Thing["score"])
    Reputations.append(Thing["reputation"])
        
    Counter += 1
        
  Overall = []
  Sorted = []
​
  Counter = 0
  Length = len(Scores)
  
  while (Counter < Length):
    Part1 = (Scores[Counter]) * 1
    Part2 = (Reputations[Counter]) * 2
    TrueScore = Part1 + Part2
    Overall.append(TrueScore)
    Sorted.append(TrueScore)
    Counter += 1
  
  Sorted = sorted(Sorted, reverse = True)
​
  Revised = []
  
  OC = 0
  OL = len(Overall)
  
  SC = 0
  SL = len(Sorted)
    
  if (Revised == []):
    RL = 0
  else:
    RL = len(Revised)
    
  while (RL < SL):
  
    Checking = Overall[OC]
    Seeking = Sorted[SC]
    
    if (Checking == Seeking):
      
      Dictionary = {}
      Dictionary["name"] = Names[OC]
      Dictionary["score"] = Scores[OC]
      Dictionary["reputation"] = Reputations[OC]
      
      Revised.append(Dictionary)
      RL = len(Revised)
      SL = len(Sorted)
      OC = 0
      SC += 1
    
    else:
      OC += 1
  
  return Revised

