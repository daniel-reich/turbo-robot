"""


Given a string indicating a range of letters, return a string which includes
all the letters in that range, _including_ the last letter. Note that if the
range is given in _capital letters_ , return the string in capitals also!

### Examples

    gimme_the_letters("a-z") ➞ "abcdefghijklmnopqrstuvwxyz"
    
    gimme_the_letters("h-o") ➞ "hijklmno"
    
    gimme_the_letters("Q-Z") ➞ "QRSTUVWXYZ"
    
    gimme_the_letters("J-J") ➞ J"

### Notes

  * A _hyphen_ will separate the two letters in the string.
  * You don't need to worry about error handling in this one (i.e. both letters will be the same case and the second letter will always be after the first alphabetically).

"""

def gimme_the_letters(spectrum):
  
  Sample = str(spectrum)
  Letters = Sample.lower()
  
  Code = " abcdefghijklmnopqrstuvwxyz"
  
  First = Letters[0]
  Last = Letters[2]
  
  Start = Code.index(First)
  End = Code.index(Last)
    
  Counter = Start
  Range = ""
  
  while (Counter <= End):
    Range = Range + Code[Counter]
    Counter += 1
  
  Test = Sample[0]
  
  if (Test.isupper()):
    Range = Range.upper()
  else:
    Range = Range
  
  return Range

