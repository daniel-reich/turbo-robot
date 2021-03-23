"""


A baseball player's batting average is calculated by the following formula:

    BA = (number of hits) / (number of official at-bats)

Batting averages are always expressed rounded to the nearest thousandth with
no leading zero. The top 3 MLB batting averages of all-time are:

  1. Ty Cobb .366
  2. Rogers Hornsby .358
  3. Shoeless Joe Jackson .356

The given list represents a season of games. Each list item indicates a
player's `[hits, official at bats]` per game. Return a string with the
player's seasonal batting average rounded to the nearest thousandth.

### Examples

    batting_avg([[0, 0], [1, 3], [2, 2], [0, 4], [1, 5]]) ➞ ".286"
    
    batting_avg([[2, 5], [2, 3], [0, 3], [1, 5], [2, 4]]) ➞ ".350"
    
    batting_avg([[2, 3], [1, 5], [2, 4], [1, 5], [0, 5]]) ➞ ".273"

### Notes

  * The number of hits will not exceed the number of official at-bats.
  * The list includes official at-bats only. No other plate-appearances (walks, hit-by-pitches, sacrifices, etc.) are included in the list.
  * HINT: Think in terms of total hits and total at-bats.

"""

def batting_avg(lst):
    hits = sum(x[0] for x in lst)
    at_bats = sum(x[1] for x in lst)
    average = str( round(hits/at_bats, 3) )[1:]
    if len(average) != 4:
        return average + '0'
    else:
        return average

