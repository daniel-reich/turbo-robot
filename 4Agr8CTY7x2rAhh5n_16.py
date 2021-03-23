"""


Create a function that takes a string and returns a string with its letters in
alphabetical order.

### Examples

    alphabet_soup("hello") ➞ "ehllo"
    
    alphabet_soup("edabit") ➞ "abdeit"
    
    alphabet_soup("hacker") ➞ "acehkr"
    
    alphabet_soup("geek") ➞ "eegk"
    
    alphabet_soup("javascript") ➞ "aacijprstv"

### Notes

You can assume numbers and punctuation symbols won't be included in test
cases. You'll only have to deal with single word, alphabetic characters.

"""

def alphabet_soup(txt):
  lst = list(txt)
  lst.sort()
  ntxt = ''
  for char in lst:
    ntxt += char
  return ntxt

