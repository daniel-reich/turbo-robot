"""


Create a function that takes a string as an argument and tells the number of
repitions of a substring. It is exactly vice versa to repeating a string
function (i.e. if a string "k" is given and asked to make a larger string "z"
such that "k" is repated "n' times).

In this scenario, we do the opposite. Given the final string, and ask the
number of times the substring is repeated.

### Examples

    number_of_repeats("abcabcabcabc" ) ➞ 4
    
    number_of_repeats("bcbcbc") ➞ 3
    
    number_of_repeats("llbllbllbllbllbllb") ➞ 6
    
    number_of_repeats("kc") ➞ 1

### Notes

  * Assume that the substring length is always greater than 1.
  * Assume that the string length is always greater than 1.
  * Assume that the substring is not always the same.

"""

class Substring:
  
  def __init__(self, substring):
    self.s = substring
  
  def repeat(self, times):
    return self.s * times
  
  def match(self, string):
    test_string = self.s
    times = 2
    while len(test_string) < len(string):
      test_string = self.repeat(times)
      times += 1
    if len(test_string) == len(string):
      if test_string == string:
        return times-1
      else:
        return False
    else:
      return False
  
  def __str__(self):
    return self.s
​
def number_of_repeats(s):
  
  substrings = []
  half_index = len(s) // 2 + 1
  
  for n in range(half_index):
    substrings.append(Substring(s[:n+1]))
  
  for substring in substrings:
    if substring.match(s) != False:
      return substring.match(s)
  
  return 1

