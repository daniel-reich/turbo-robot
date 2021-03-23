"""


Create a function which replaces all the x's in the string in the following
ways:

Replace all x's with "cks" **UNLESS** :

  * The word begins with "x", therefore replace it with "z".
  * The word is just the letter "x", therefore replace it with "ecks".

### Examples

    x_pronounce("Inside the box was a xylophone") ➞ "Inside the bocks was a zylophone"
    
    x_pronounce("The x ray is excellent") ➞ "The ecks ray is eckscellent"
    
    x_pronounce("OMG x box unboxing video x D") ➞ "OMG ecks bocks unbocksing video ecks D"

### Notes

  * All x's are lowercase.
  * I know that not all words with x's follow this rule, but there are too many edge cases to count!

"""

def x_pronounce(sentence):
  s = sentence.split()
  new_sentence = ""
  for word in s:
    if word == 'x':
      new_sentence += 'ecks '
    elif word[0] == 'x':
      new_sentence += 'z' + word[1:] + " "
    elif 'x' in word:
      new_sentence += word.replace('x','cks') + " "
    else:
      new_sentence += word + " "
  return new_sentence.rstrip()

