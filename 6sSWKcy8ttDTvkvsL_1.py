"""


If today was Monday, in two days, it would be Wednesday.

Create a function that takes in a list of days as input and the number of days
to increment by. Return a list of days after `n` number of days has passed.

### Examples

    after_n_days(["Thursday", "Monday"], 4) ➞ ["Monday", "Friday"]
    
    after_n_days(["Sunday", "Sunday", "Sunday"], 1) ➞ ["Monday", "Monday", "Monday"]
    
    after_n_days(["Monday", "Tuesday", "Friday"], 1) ➞ ["Tuesday", "Wednesday", "Saturday"]

### Notes

  * Return as a list.
  * All test cases will have the first letter of each day capitalized.
  * `n` number of days may be greater than 7.

"""

from calendar import day_name
def afterNdays(days, n):
  lst = list(day_name)
  return [lst[(lst.index(i) + n) % 7] for i in days]

