"""


As you complete questions on Edabit, you gain experience points depending on
the difficulty of the question. The points for each difficulty are as follows:

Difficulty| Experience Points  
---|---  
Very Easy| 5XP  
Easy| 10XP  
Medium| 20XP  
Hard| 40XP  
Very Hard| 80XP  
  
Given a dictionary of how many questions a person has completed of each
difficulty, return **how many experience points** they'll have.

### Examples

    get_xp({
      "Very Easy" : 89,
      "Easy" : 77,
      "Medium" : 30,
      "Hard" : 4,
      "Very Hard" : 1
    }) ➞ "2055XP"
    get_xp({
      "Very Easy" : 254,
      "Easy" : 32,
      "Medium" : 65,
      "Hard" : 51,
      "Very Hard" : 34
    }) ➞ "7650XP"
    get_xp({
      "Very Easy" : 11,
      "Easy" : 0,
      "Medium" : 2,
      "Hard" : 0,
      "Very Hard" : 27
    }) ➞ "2255XP"

### Notes

Return values as a string and make sure to add "XP" to the end.

"""

def get_xp(d):
  sum = 0
  for key,val in d.items():
    if key == "Very Easy":
      pts = 5
    elif key == "Easy":
      pts = 10
    elif key == "Medium":
      pts = 20
    elif key == "Hard":
      pts = 40
    else:
      pts = 80
    sum = sum + pts*val
  return str(sum)+"XP"

