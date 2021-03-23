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
  try:
    vowels = ["A", "E", "I", "O", "U", "a","e","i","o","u"]
    txtlst = txt.split(" ")
    newlst = []
    for word in txtlst:
      if word[0] in vowels:
        newlst.append(word.lower().strip("."))
    return newlst
  except:
    return []

