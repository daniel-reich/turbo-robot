"""


And who cursed the most in the fight between you and your spouse?

Given a **dict** with three rounds, with nested **dict** s as your score per
round, return who cursed the most based on the following:

  * If you, return "ME!"
  * If your spouse, return "SPOUSE!"
  * If a draw, return "DRAW!"

### Examples

    determine_who_cursed_the_most({
      "round1": { "me": 10, "spouse": 5 },
      "round2": { "me": 5, "spouse": 10 },
      "round3": { "me": 10, "spouse": 10 }}) ➞ "DRAW!"
    
    determine_who_cursed_the_most({
      "round1": { "me": 40, "spouse": 5 },
      "round2": { "me": 9, "spouse": 10 },
      "round3": { "me": 9, "spouse": 10 }}) ➞ "ME!"
    
    determine_who_cursed_the_most({
      "round1": { "me": 10, "spouse": 5 },
      "round2": { "me": 9, "spouse": 44 },
      "round3": { "me": 10, "spouse": 55 }}) ➞ "SPOUSE!"

### Notes

N/A

"""

def determine_who_cursed_the_most(d):
  
  My_Swearing_Numbers = []
  Spouse_Swearing_Numbers = []
  
  Counter = 0
  Length = len(d)
  
  Item = d["round1"]
  My_Swearing_Numbers.append(Item["me"])
  Spouse_Swearing_Numbers.append(Item["spouse"])
  
  Item = d["round2"]
  My_Swearing_Numbers.append(Item["me"])
  Spouse_Swearing_Numbers.append(Item["spouse"])
  
  Item = d["round3"]
  My_Swearing_Numbers.append(Item["me"])
  Spouse_Swearing_Numbers.append(Item["spouse"])
    
  My_Total = 0
  
  for x in My_Swearing_Numbers:
    My_Total += x
  
  Spouse_Total = 0
  
  for x in Spouse_Swearing_Numbers:
    Spouse_Total += x
  
  if (My_Total > Spouse_Total):
    return "ME!"
  elif (Spouse_Total > My_Total):
    return "SPOUSE!"
  else:
    return "DRAW!"

