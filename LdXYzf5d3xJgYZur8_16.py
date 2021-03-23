"""


Create a function that takes three values:

  * `h` hours
  * `m` minutes
  * `s` seconds

Return the value that's the **longest duration**.

### Examples

    longest_time(1, 59, 3598) ➞ 1
    
    longest_time(2, 300, 15000) ➞ 300
    
    longest_time(15, 955, 59400) ➞ 59400

### Notes

No two durations will be the same.

"""

def longest_time(h, m, s):
  if h*60>m and h*60*60>s:
    return h
  elif m>h*60 and m*60>s:
    return m
  else:
    return s

