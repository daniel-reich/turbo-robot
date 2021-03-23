"""


This is a list of single characters with an unwanted character at the end:

    ["H", "e", "l", "l", "o", "!", "\0"]

You could also just type "Hello!" when initializing a variable, creating the
string "Hello!"

Create a function that will return a string by combining the given character
list, not including the unwanted final character.

### Examples

    cpp_txt(["H", "i", "!", "\0"]) ➞ "Hi!"
    
    cpp_txt(["H", "e", "l", "l", "o", "!", "\0"]) ➞ "Hello!"
    
    cpp_txt(["J", "A", "V", "a", "\0"]) ➞ "JAVa"

### Notes

This is a translation of a C++ challenge and is trivial in Python, but perhaps
it will be helpful to someone out there. (No challenge is trivial until you
know how to solve it :)

"""

def cpp_txt(lst):
  lst.pop()
  s = ""
  return s.join(lst)

