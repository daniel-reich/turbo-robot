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
  #convert all to seconds
  h2s = h * 3600
  m2s = m * 60
  if max(h2s,m2s,s) == h2s:
    return h
  elif max(h2s,m2s,s) == m2s:
    return m
  return s

