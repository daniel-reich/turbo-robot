"""


Your job is to make a "Twitter link" regular expression `rx`. This RegEx
searches a tweet to find the **@handle** and the **#handle**. Only return the
**@** and **#** handles.

### Examples

    tweet("Visit us at @edabit") ➞ "@edabit"
    
    tweet("Follow @JavaScript") ➞ "@JavaScript"
    
    tweet("#Honesty is the best @policy!!") ➞ "#Honesty @policy"

### Notes

Make sure the RegEx doesn't return `.` `,` `!` `?`, etc.

"""

def tweet(txt):
  res = []
  t = txt.split()
  for k in range(0, len(t)):
    if t[k].startswith("#") or t[k].startswith("@"):
      res.append(t[k].strip(".").strip(",").strip("?").strip("!"))
  return " ".join(res)

