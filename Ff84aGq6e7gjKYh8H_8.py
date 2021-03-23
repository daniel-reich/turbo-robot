"""


You are given the length of a video in minutes. The format is **mm:ss** (e.g.:
`"02:54"`). Create a function that takes the _video length_ and return it in
**seconds**.

### Examples

    minutes_to_seconds("01:00") ➞ 60
    
    minutes_to_seconds("13:56") ➞ 836
    
    minutes_to_seconds("10:60") ➞ False

### Notes

  * The video length is given as a string.
  * If the number of seconds is **60 or over** , return `False` (see example #3).
  * You may get a number of minutes over 99 (e.g. `"121:49"` is perfectly **valid** ).

"""

def minutes_to_seconds(time):
  t = time.split(":")
  return int(t[0])*60+int(t[-1]) if int(t[-1]) < 60 else False

