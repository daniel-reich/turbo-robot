"""


Write a function, that replaces all vowels in a string with a specified vowel.

### Examples

    vow_replace("apples and bananas", "u") ➞ "upplus und bununus"
    
    vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"
    
    vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"

### Notes

All words will be lowercase. Y is not considered a vowel.

"""

def vow_replace(word, vowel):
  cum = list(word)
  boom = []
  for x in cum:
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
      boom.append(vowel)
    else:
      boom.append(x)
  return "".join(boom)

