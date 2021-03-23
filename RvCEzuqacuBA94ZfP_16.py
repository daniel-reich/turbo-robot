"""


Create a function that is a Hashtag Generator by using the following rules:

  * The output must start with a hashtag (#).
  * Each word in the string must have its first letter capitalized.
  * If the final result, a single string, is longer than 140 characters, the function should return `false`.
  * If either the input (`str`) or the result is an empty string, the function should return `false`.

### Examples

    generate_hashtag("    Hello     World   " ) ➞ "#HelloWorld"
    
    generate_hashtag("") ➞ false, "Expected an empty string to return false"
    
    generate_hashtag("Edabit Is Great") ➞ "#EdabitIsGreat", "Should remove spaces."

### Notes

N/A

"""

from re import sub
def generate_hashtag(txt):
  txt = sub(r'(?<!\S)([a-z])',lambda x: x.group(1).upper(),txt)
  txt = sub(r'\s+','',txt)
  if len(txt) >= 139 or len(txt) == 0:
    return False
  return "#" + txt

