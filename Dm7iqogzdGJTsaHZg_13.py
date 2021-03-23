"""


Write a function that retrieves all words that begin with a vowel.

### Examples

    retrieve("A simple life is a happy life for me.") ➞ ["a", "is", "a"]
    
    retrieve("Exercising is a healthy way to burn off energy.")
    ➞ ["exercising", "is", "a", "off", "energy"]
    
    retrieve("The poor ostrich was ostracized.")
    ➞ ["ostrich", "ostracized"]
    
    retrieve("")
    ➞ []

### Notes

  * Make all words lower case in the output.
  * Retrieve the words in the order they appear in the sentence.

"""

def retrieve(txt):
  vowels = ["a", "e", "i", "o", "u", "y"]
  output = list()
  for word in txt.lower().strip(".").split():
    for vowel in vowels:
      if word.startswith(vowel):
        output.append(word)
  return output

