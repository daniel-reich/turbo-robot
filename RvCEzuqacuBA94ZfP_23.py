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
  hashtag = "#"
  print(txt)
  txt = txt.split()
  print(type(txt))
  if not txt:
    return False
  for i in range(len(txt)):
    txt[i] = txt[i].replace(txt[i], txt[i].lower())
  for i in range(len(txt)):
    txt[i] = txt[i].replace(txt[i][0], txt[i][0].upper(),1)
  for s in txt:
    hashtag += s
  if len(hashtag) > 140:
    return False
  print(hashtag)
  return hashtag

