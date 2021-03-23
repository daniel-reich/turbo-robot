"""


Write a function that takes a string and calculates the number of letters and
digits within it. Return the result in a dictionary.

### Examples

    count_all("Hello World") ➞ { "LETTERS":  10, "DIGITS": 0 }
    
    count_all("H3ll0 Wor1d") ➞ { "LETTERS":  7, "DIGITS": 3 }
    
    count_all("149990") ➞ { "LETTERS": 0, "DIGITS": 6 }

### Notes

  * Tests contain only alphanumeric characters.
  * Spaces are not letters.
  * All tests contain valid strings.

"""

def count_all(txt):
  m={}
  ch,dig=0,0
  for x in txt:
    if x.isdigit():
      dig+=1
    elif 65<=ord(x)<=91 or 97<=ord(x)<=123:
      ch+=1
  m["LETTERS"]=ch
  m["DIGITS"]=dig
  return m

