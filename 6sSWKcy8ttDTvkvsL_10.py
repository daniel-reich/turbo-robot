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

def afterNdays(days, n):
  days2int = { "Sunday" : 0, 
               "Monday" : 1,
               "Tuesday" : 2,
               "Wednesday" : 3,
               "Thursday" : 4,
               "Friday" : 5,
               "Saturday" : 6 }
  int2days = { 0 : "Sunday",
               1 : "Monday",
               2 : "Tuesday",
               3 : "Wednesday",
               4 : "Thursday",
               5 : "Friday",
               6 : "Saturday" }
  return [ int2days[(days2int[day] + n) % 7] for day in days ]

