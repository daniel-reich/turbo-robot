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
  return ' '.join(x.strip('.,!?') for x in txt.split(' ') if x[0] == '#' or x[0] == '@')

