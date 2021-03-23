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

def dailyStreak(lst):
  cur_daily, daily = 0, 0
  for i,x in enumerate(lst):
    if x == True:
      if i == 0:
        cur_daily = 1
        daily = 1
      elif lst[i-1] == False:
        cur_daily += 1
      elif lst[i-1] == True:
        cur_daily += 1
        if cur_daily > daily:
          daily = cur_daily
    else:
      cur_daily = 0
  return daily

