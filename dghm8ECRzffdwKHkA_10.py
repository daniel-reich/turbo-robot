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
  return sum([1 for x in txt if x == x.upper()])

