"""


Write a function that converts `hours` into seconds.

### Examples

    how_many_seconds(2) ➞ 7200
    
    how_many_seconds(10) ➞ 36000
    
    how_many_seconds(24) ➞ 86400

### Notes

  * 60 seconds in a minute, 60 minutes in an hour
  * Don't forget to `return` your answer.

"""

def how_many_seconds(hours):
    seconds=hours*60*60
    return seconds

