"""


Using Camel Case (or camelCase) is where the first word is in lower case, and
all words after it have their first letter capitalised. Note that there are no
spaces in between words!

Create a function that takes a string and returns it back in camelCase.

### Examples

    camelCasing("Hello World") ➞ "helloWorld"
    
    camelCasing("snake_case") ➞ "snakeCase"
    
    camelCasing("low high_HIGH") ➞ "lowHighHigh"

### Notes

  * You need to remove all spaces and underscores.
  * There will be no numbers in inputs.

"""

def camelCasing(txt):
  new_txt = txt.replace("_", " ").split()
  new_sentence_lst = []
  count = 0
  for word in new_txt:
    if count == 0:
      new_sentence_lst.append(word.lower())
    else:
      new_sentence_lst.append(word.capitalize())
    count += 1
  return "".join(new_sentence_lst)

