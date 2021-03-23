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

def cal(length):
  res = length // 150 
  total = res * 30 + length 
  if length != 150:
    res = (total / 150) * 30 + (res * 10)
  else:
    return 30
  res = str(res).split('.')
  if res[-1] == '0':
    pass
  else:
    res[0] = int(res[0]) + 1
  return (int(res[0]))

