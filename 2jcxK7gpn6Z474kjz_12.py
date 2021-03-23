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
  filtered = [char for char in txt if char in 'TG$']
  for index, char in enumerate(filtered):
    if char != '$':
      continue
    if index > 0 and filtered[index - 1] == 'T':
      return 'ALARM!'
    if index < len(filtered) - 1 and filtered[index + 1] == 'T':
      return 'ALARM!'
  return 'Safe'

