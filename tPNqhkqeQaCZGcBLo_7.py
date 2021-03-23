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
    me = sum([d['round' + str(_ + 1)]['me'] for _ in range(len(d))])
    sp = sum([d['round' + str(_ + 1)]['spouse'] for _ in range(len(d))])
    if me > sp:
        return 'ME!'
    elif sp > me:
        return 'SPOUSE!'
    else:
        return 'DRAW!'

