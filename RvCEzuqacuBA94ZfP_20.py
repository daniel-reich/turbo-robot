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

def generate_hashtag(txt):
  strip_txt = txt.strip()
  if strip_txt == '':
    return False
  split_txt = strip_txt.split(' ')
  merge_txt = ''
  for i in split_txt:
    if i != '':
      merge_txt += i.capitalize()
  hash_txt = '#'+merge_txt
  if len(hash_txt) > 140:
    return False
  return hash_txt

