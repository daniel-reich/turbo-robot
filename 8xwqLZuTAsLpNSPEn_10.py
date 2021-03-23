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

def award_prizes(dic):
    inv_dic = {v: k for k, v in dic.items()}
    name = []
    a = []
    partc = []
    for i in dic.values():
        a = a + [i]
        a.sort()
    for i in a: 
        if i in inv_dic.keys():
            name = name + [inv_dic[i]]
        namelen = len(name)
    for p in range(0, (namelen-3)):
        partc = partc + [name[p]]
    first_place = name[-1]
    second_place = name[-2]
    third_place = name[-3] 
​
    winners = {}
    winners.setdefault(first_place, "Gold")
    winners.setdefault(second_place, "Silver")
    winners.setdefault(third_place, "Bronze")
    for i in partc:
        winners.setdefault(i, "Participation")
    return winners

