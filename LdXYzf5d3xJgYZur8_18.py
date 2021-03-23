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
  time = {h : h,
          m : (m // 60),
          s : (s // 3600)
          }
​
  return [k for k,v in time.items() if max(time.values()) == v][0]

