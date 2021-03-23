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
  lst = []
  vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  a = txt.split()
  if txt == "":
    return []
  for b in a:
    if b.startswith('a') == True or b.startswith('i') == True or b.startswith('e') == True or b.startswith('o') == True or b.startswith('u') == True or b.startswith('A') == True or b.startswith('E') == True or b.startswith('I') == True or b.startswith('O') == True or b.startswith('U') == True:  
      lst.append(b.lower())
  if lst[-1].endswith("."):
    x = lst[-1]
    lst.remove(x)
    lst.append(x[0:-1])
  return lst

