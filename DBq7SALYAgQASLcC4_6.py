"""


Create a function that takes two strings as arguments and returns the number
of times the first string (the single character) is found in the second
string.

### Examples

    char_count("a", "edabit") ➞ 1
    
    char_count("c", "Chamber of secrets") ➞ 1
    
    char_count("b", "big fat bubble") ➞ 4

### Notes

Your output must be case-sensitive (see second example).

"""

def char_count(txt1, txt2):
  output = txt2.count(txt1)
  return output

