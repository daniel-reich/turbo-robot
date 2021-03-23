"""


![](https://edabit-challenges.s3.amazonaws.com/segment4.gif)

The table below shows which of the segments `a` through `g` are illuminated on
the seven segment display for the digits `0` through `9`. When the number on
the display changes, some of the segments may stay on, some may stay off, and
others change state (on to off, or off to on).

Create a function that accepts a string of digits, and for each transition of
one digit to the next, returns a list of the segments that change state.
Designate the segments that turn on as uppercase and those that turn off as
lowercase. Sort the lists in alphabetical order.

For example:

    seven_segment("805") ➞ [["g"], ["b", "e", "G"]]

In the transition from `8` to `0`, the `g` segment turns off. Others are
unchanged. In the transition from `0` to `5`, `b` and `e` turn off and `G`
turns on. Others are unchanged.

Digit| Lit Segments  
---|---  
0| abcdef  
1| bc  
2| abdeg  
3| abcdg  
4| bcfg  
5| acdfg  
6| acdefg  
7| abc  
8| abcdefg  
9| abcfg  
  
### Examples

    seven_segment("02") ➞ [["c", "f", "G"]]
    
    seven_segment("08555") ➞ [["G"], ["b", "e"], [], []]
    # Empty lists designate no change.
    
    seven_segment("321") ➞ [["c", "E"], ["a", "C", "d", "e", "g"]]
    
    seven_segment("123") ➞ [["A", "c", "D", "E", "G"], ["C", "e"]]
    
    seven_segment("3") ➞ []
    
    seven_segment("33") ➞ [[]]

### Notes

N/A

"""

def seven_segment(txt):
  
  class Digit:
​
    def __init__(self, digit):
​
      self.digit = int(digit)
​
      if self.digit == 0:
        self.on = list('abcdef')
      elif self.digit == 1:
        self.on = list('bc')
      elif self.digit == 2:
        self.on = list('abdeg')
      elif self.digit == 3:
        self.on = list('abcdg')
      elif self.digit == 4:
        self.on = list('bcfg')
      elif self.digit == 5:
        self.on = list('acdfg')
      elif self.digit == 6:
        self.on = list('acdefg')
      elif self.digit == 7:
        self.on = list('abc')
      elif self.digit == 8:
        self.on = list('abcdefg')
      elif self.digit == 9:
        self.on = list('abcfg')
​
    def differences(self, other):
​
      changes = []
​
      for item in self.on:
        if item not in other.on:
          changes.append(item.lower())
      for item in other.on:
        if item not in self.on:
          changes.append(item.upper())
      
      return sorted(changes, key=str.lower)
 
  digits = []
​
  for item in list(txt):
    digits.append(Digit(item))
  
  changes = []
​
  for n in range(len(digits) - 1):
    d1 = digits[n]
    d2 = digits[n+1]
    changes.append(d1.differences(d2))
  
  return changes

