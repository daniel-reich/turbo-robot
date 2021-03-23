"""


You're head of security at a casino that has money being stolen from it. You
get the data in the form of strings and you have to set off an alarm if a
thief is detected.

  * If there is no guard between thief and money, return `"ALARM!"`
  * If the money is protected, return `"Safe"`

### String Components

  * x - Empty Space
  * T - Thief
  * G - Guard
  * $ - Money

### Examples

    security("xxxxTTxGxx$xxTxxx") ➞ "ALARM!"
    
    security("xxTxxG$xxxx$xxxx") ➞ "Safe"
    
    security("TTxxxx$xxGxx$Gxxx") ➞ "ALARM!"

### Notes

Money at the extremes are safe.

"""

def security(txt):
  alarm = False
  casino = list(txt)
  while "x" in casino:
    casino.remove("x")
  for i in range(len(casino)):
    if casino[i] == "$":
      if i == 0:
        if casino[1] == "T":
          alarm = True
      elif i == len(casino) - 1:
        if casino[-2] == "T":
          alarm = True
      else:
        if casino[i - 1] == "T" or casino[i + 1] == "T":
          alarm = True
  if alarm:
    return "ALARM!"
  else:
    return "Safe"

