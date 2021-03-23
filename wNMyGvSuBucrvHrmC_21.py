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

def only_consists_of_substring(string, substring):
  count = len(string) // len(substring)
  mult_string = substring * count
  return mult_string == string
​
def number_of_repeats(string):
  for i in range(1, len(string) + 1):
    substring = string[:i]
    result = only_consists_of_substring(string, substring)
    if result == True:
      return len(string) // len(substring)

