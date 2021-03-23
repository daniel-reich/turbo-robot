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

def daily_streak(l):
        temp = 0
        m = 0
        for i in range(len(l)):
            print(l[i])
            if l[i]:
                temp += 1
            else:
                if m < temp:
                    m = temp
                temp = 0
        if temp > m:
            m = temp
        return(m)

