"""


A word value can be established summing up all the numeric values of every
single character (excluding spaces and punctuation): a value from 1 ("a") to
26 ("z") is given to letters, while numbers have their literal values, from 0
to 9. The sentence value is the sum of the values of the words.

    sentence = "ABC ! abc ... @ 123"
    # Remove spaces, punctuation and any symbol.
    
    sentence = ["ABC", "abc", "123"]
    
    words values = "ABC" = 1+2+3 = 6 | "abc" = 1+2+3 = 6 | "123" = 1+2+3 = 6
    
    sentence value = 6 + 6 + 6 = 18

Given a string `sentence` implement a function that returns:

  * `Prime Sentence` if the original sentence value is a prime.

  * `Almost Prime Sentence (xxx)` if the sentence value is not a prime but, after a single removal of any of the words the new sentence value is a prime (see example #2 for a clearer explanation), with _xxx_ being the word removed. If more than a word can be removed to obtain a prime value, return the first encountered in the original sentence.

  * `Composite Sentence` if the sentence value is not a prime and more than one removal is necessary to make the new sentence value (or if none is possible).

Letters values are case insensitive ("aZ" = "Az" = 1 + 26 = 27), while numbers
are treated as words ("123" = 1+2+3 = 6).

### Examples

    sentence_primeness("Help me!") ➞ "Prime Sentence"
    # "Help" + "me" = 41 + 18 = 59 (prime)
    
    sentence_primeness("42 is THE aNsWeR...") ➞ "Almost Prime Sentence (aNsWeR)
    # "42" + "is" + "THE" + "aNsWeR" = 6 + 28 + 33 + 80 = 147 (not prime)
    # Without "42" new value is 141
    # Without "is" new value is 119
    # Without "THE" new value is 114
    # Without "aNsWeR" new value is 67 (prime!)
    # If the word "aNsWeR" is removed from sentence the new value is a prime.
    
    sentence_primeness("Did you smoke?") ➞ "Composite Sentence"
    # "Did" + "you" + "smoke" = 17 + 61 + 63 = 141 (not prime)
    # Without "Did" new value is 124
    # Without "you" new value is 80
    # Without "smoke" new value is 78
    # No single removals make the new sentence value a prime.

### Notes

  * Only letters and digits can be part of the sentence.
  * If it's an Almost Prime Sentence, the removed word between the brackets must maintain the same capitalization format found in the original sentence (see example #2).
  * The sentence is Almost Prime if just a single word can be removed to make value a prime, no multiple removals allowed.
  * Remember the rule for numbers: "10" is a word, so its value is 1+0 and not 10.

"""

import re
import string
​
def sentence_primeness(sentence):
​
  #functions
  def prime(x):
      if x == 4:
          return False
      for i in range(2, x//2):
          if x % i == 0:
              return False
      return True
​
  #setup
  invalidCharacters = []
  wordValues = []
  lowerCase = list(string.ascii_lowercase)
  lowerCase.insert(0, "")
  upperCase = list(string.ascii_uppercase)
  upperCase.insert(0, "")
  digits = list(string.digits)
​
  #removes every non alphanumeric character
  sentence = re.sub(r"[^a-zA-Z0-9 ]", "", sentence)
​
  #splits string into individual words
  sentence = sentence.split(" ")
​
  #removes unneccessary list items
  while "" in sentence:
      sentence.remove("")
​
  #calculates sentence and word values
  sentenceValue = 0
  for word in sentence:
      wordValue = 0
      for c in word:
          for i in lowerCase:
              if i == c:
                  wordValue += lowerCase.index(i)
          for i in upperCase:
              if i == c:
                  wordValue += upperCase.index(i)
          for i in digits:
              if i == c:
                  wordValue += digits.index(i)
      wordValues.append(wordValue)
      sentenceValue += wordValue
​
  #prime sentence
  if prime(sentenceValue) == True:
      return "Prime Sentence"
​
  #almost prime sentence
  for value in wordValues:
      if prime(sentenceValue - value) == True:
          return "Almost Prime Sentence (" + sentence[wordValues.index(value)] + ")"
​
  #composite sentence
  return "Composite Sentence"

