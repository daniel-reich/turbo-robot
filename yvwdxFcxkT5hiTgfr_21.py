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
    d2={'Very Easy':5,
        'Easy':10,
        'Medium':20,
        'Hard':40,
        'Very Hard':80}
    a=list(d2.values())
    b=list(d.values())
    return str(sum([x*i for x,i in zip(a,b)]))+'XP'

