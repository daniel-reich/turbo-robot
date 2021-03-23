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

import re
​
def tweet(txt):
  txt_list = txt.split(" ")
  t = []
  for i in txt_list:
    if '@' in i or '#' in i:  
      i = re.sub(r'[^\w' + '@#' + ']', '', i)
      t.append(i)
  return " ".join(t)

