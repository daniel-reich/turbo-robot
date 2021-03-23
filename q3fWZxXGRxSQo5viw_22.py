"""


A snail fell into a bucket and wanted to crawl out. Assuming we already know
the snail can climb 5cm per minute, the snail can crawl for 30 minutes
continuously and then needs to rest for 10 minutes. When it is resting it will
slide down 30cm.

How many minutes will it take for the snail to crawl out from different
depths? Create a function that takes the bucket depth (the unit is cm) as an
argument and returns the time in minutes.

    if depth = 270
    the snail crawling process
    process: (150 - 30) +  150
    minutes: (30+10) + 150 / 5
    it will take 70 minutes
    the last 150cm, the snail doesn't need a rest

### Examples

    cal(31) ➞ 7
    
    cal(150) ➞ 30
    
    cal(200) ➞ 56

### Notes

  * The depth is a positive integer.
  * If the time is less than one minute it still counts as one minute.

"""

def cal(d):
  # 5 cm / h
  # it can crawl for 30 mins
  # 10 mins rest and slides down 30 cms
  s = 5
  t = 30
  r = 10
  b = 30
  a = 0
  while d >= 0:
    for i in range(t):
      if d<=0: return a
      d -= s
      a += 1
    for i in range(r):
      if d<=0: return a
      a += 1
    if d >= 0:
      d += 30
  return a

