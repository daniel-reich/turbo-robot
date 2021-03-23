"""


In this challenge you are given a string and a slice made from that string.
Make a function that returns an expression that can be used to make that
slice. Your answer must contain only the minimum number of keystrokes needed
to make the slice.

### Examples

    slicer("abcd", "b") ➞ "[1]"
    
    slicer("abcdefg", "cb") ➞ "[2:0:-1]"
    
    slicer("abcdefg", "be") ➞ "[1::3]"
    
    slicer("abcdefgh", "bdf") ➞ "[1:6:2]"

### Notes

  * Test cases are slices that can be made with the `[start:end:step]` type expression.
  * The strings are composed of unique characters (no repeats).

"""

class Slicer:
  def __init__(self,string,slic):
    self.string = string
    self.slic = slic
    self.size = string.find(slic[1]) - string.find(slic[0])
    self.start = string.find(slic[0])
    if self.size > 0:
      self.end = string.find(slic[-1]) + 1
    else:
      self.end = string.find(slic[-1]) - 1
  def s(self):
    return self.string[self.start::self.size]
  def string1(self):
    if self.start == 0 and self.size > 0:
      return ""
    elif self.start == len(self.string) - 1 and self.size < 0:
      return ""
    else:
      return str(self.start)
  def string2(self):
    if self.slic[-1] == self.s()[-1]:
      return ""
    else:
      return str(self.end)
  def string3(self):
    return "" if self.size == 1 and len(self.string2()) > 0 else ":"
  def string4(self):
    return "" if self.size == 1 else str(self.size)
    
    
def slicer(string, slic):
  if string == slic:
    return "[:]"
  elif len(slic) == 1:
    return "[{}]".format(str(string.find(slic)))
  else:
    s = Slicer(string,slic)
    return "[{}:{}{}{}]".format(s.string1(),s.string2(),s.string3(),s.string4())

