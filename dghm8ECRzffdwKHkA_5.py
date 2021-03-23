"""


Given a string of letters, how many **capital letters** are there?

### Examples

    capital_letters("fvLzpxmgXSDrobbgMVrc") ➞ 6
    
    capital_letters("JMZWCneOTFLWYwBWxyFw") ➞ 14
    
    capital_letters("mqeytbbjwqemcdrdsyvq") ➞ 0

### Notes

N/A

"""

def capital_letters(txt):
 upper = 0
 for i in range(len(txt)):
   if (ord(txt[i]) >= 65 and
     ord(txt[i]) <= 90):
      upper += 1
 return upper

