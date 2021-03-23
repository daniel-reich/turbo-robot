"""


You are given a dictionary of _names_ and the amount of _points_ they have.
Return a dictionary with the same names, but instead of points, return what
prize they get.

`"Gold"`, `"Silver"`, or `"Bronze"` to the 1st, 2nd and 3rd place
respectively. For all the other names, return `"Participation"` for the prize.

### Examples

    award_prizes({
      "Joshua" : 45,
      "Alex" : 39,
      "Eric" : 43
    }) ➞ {
      "Joshua" : "Gold",
      "Alex" : "Bronze",
      "Eric" : "Silver"
    }
    
    award_prizes({
      "Person A" : 1,
      "Person B" : 2,
      "Person C" : 3,
      "Person D" : 4,
      "Person E" : 102
    }) ➞ {
      "Person A" : "Participation",
      "Person B" : "Participation",
      "Person C" : "Bronze",
      "Person D" : "Silver",
      "Person E" : "Gold"
    }
    
    award_prizes({
      "Mario" : 99,
      "Luigi" : 100,
      "Yoshi" : 299,
      "Toad" : 2
    }) ➞ {
      "Mario" : "Bronze",
      "Luigi" : "Silver",
      "Yoshi" : "Gold",
      "Toad" : "Participation"
    }

### Notes

  * There will always be at least three participants to recieve awards.
  * No number of points will be the same amongst participants.

"""

def award_prizes(names):
  participants = sorted(names.keys(),key = lambda x: names[x],reverse = True)
  prizes = {x: 'Participation' for x in names.keys()}
  prizes[participants[0]] = 'Gold'
  prizes[participants[1]] = 'Silver'
  prizes[participants[2]] = 'Bronze'
  return prizes

