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
  words = txt.split(' ')
  output = []
  for word in words:
    if word[0] in ('#@'):
      output.append(word)
  links = ' '.join(output)
  outstring = ''
  for i in links:
    if i.isalpha() or i in '#@ ':
      outstring += i
  return outstring

