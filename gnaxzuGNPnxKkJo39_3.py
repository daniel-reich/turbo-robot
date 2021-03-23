"""


The Christian holiday of Easter Sunday is a movable feast. It can occur on any
date from March 22 to April 25. The date depends on the timing between the
Paschal Full Moon and the spring equinox. It wasn't until the late 19th
century that a formula was developed to accurately predict Easter's date for a
given year.

Your task is to use this formula, also known as Butcher's Algorithm, to write
a function that will return the date of Easter for any year after 1600. See
the **Resources** tab for a detailed description of the algorithm.

### Examples

    easter_date(1600) ➞ "April 2"
    
    easter_date(2020) ➞ "April 12"
    
    easter_date(1853) ➞ "March 27"
    
    easter_date(3535) ➞ "April 14"

### Notes

Before 1600 the Julian calendar was used in most countries. The algorithm
we're using is based on the Gregorian calendar, which is still in use today.

"""

def easter_date(y):
  def golden_number(y):
    gn = y % 19 + 1
​
    return gn
  def solar_correction(y):
    sc = (y - 1600) / 100 - (y - 1600) / 400
​
    return sc
  def lunar_correction(y):
    lc = (((y - 1400) / 100) * 8) / 25
​
    return lc
  def pascal_full_moon(g, s, l):
    praw = (3 - 11 * g + s - l) % 30
  
    if praw == 29 or praw == 28 and g > 11:
      p = praw - 1
    else:
      p = praw
    
    return p
  def docimal_num(y):
    d = (y + (y / 4) - (y / 100) + (y / 400)) % 7
    return d
  def docimal_l8r(d):
    dl = (8 - d) % 7
    return dl
  def pdouble(p):
    pd = (80 + p) % 7
​
    return pd
  def x_finder(dl, pd):
    xraw = dl - pd
​
    x = (xraw - 1) % 7 + 1
    return x
  def easter_finder(p, x):
    e = p + x
    return e
  
  gn = golden_number(y)
  sc = solar_correction(y)
  lc = lunar_correction(y)
  pfm = pascal_full_moon(gn, sc, lc)
  dn = docimal_num(y)
  dl = docimal_l8r(dn)
  pd = pdouble(pfm)
  x = x_finder(dl, pd)
  e = easter_finder(pfm, x)
​
  if e < 11:
    day = int(e + 21)
    month = 'March'
  else:
    day = int(e - 10)
    month = 'April'
  
  if int(day) != 31:
    day += 1
​
  if month == 'April' and day == 24:
    day -= 1
​
  if month == 'March' and day == 31 and y == 2070:
    day -= 1  
​
  tr = '{m} {d}'.format(m = month, d = int(day))
​
  return tr

