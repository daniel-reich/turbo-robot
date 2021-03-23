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
    txt_x = ''
    for letter in txt:
        if letter != 'x':
            txt_x += letter
    for i in range(1, len(txt_x) - 1):
​
        if txt_x[i] == '$':
            if txt_x[i + 1] == 'T' or txt_x[i - 1] == 'T':
                return "ALARM!"
    return "Safe"

