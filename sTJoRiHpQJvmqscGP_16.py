"""


Create a function that takes a list of booleans that represent whether or not
a player has logged into a game that day. Output the longest streak of
consecutive logged in days.

### Examples

    daily_streak([True, True, False, True]) ➞ 2
    
    daily_streak([False, False, False]) ➞ 0
    
    daily_streak([True, True, True, False, True, True]) ➞ 3

### Notes

  * Return your output as an integer.
  * If a given list is all `False`, return `0` (see example #2).

"""

def daily_streak(lst):
  a = ''.join([str(i) for i in lst]).split('False')
  return max(i.count('True') for i in a)

