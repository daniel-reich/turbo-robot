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
    d={3600*h:h,60*m:m,s:s}
    return d.get(max(d.keys()))

