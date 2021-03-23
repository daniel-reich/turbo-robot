"""


Write a function that will return the **longest word** in a sentence. In cases
where more than one word is found, return the first one.

### Examples

    find_longest("A thing of beauty is a joy forever.") ➞ "forever"
    
    find_longest("Forgetfulness is by all means powerless!") ➞ "forgetfulness"
    
    find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel.") ➞ "strengths"

### Notes

  * Special characters and symbols _don't count_ as part of the word.
  * Return the longest word found in **lowercase** letters.
  * A recursive version of this challenge can be found in [here](https://edabit.com/challenge/LyzKTyYdKF4oDf5bG).

"""

def find_longest(sentence):
  for char in sentence:
    if not char.isalpha() and char != ' ':
      sentence = sentence.replace(char, ' ')
  result = sorted(sentence.split(), key=len, reverse=True)
  return result[0].lower()

