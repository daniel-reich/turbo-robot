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
  return len([i for i in txt if i.isupper()])

