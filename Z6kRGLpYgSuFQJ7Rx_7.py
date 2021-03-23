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
  sentence = sentence.replace("'", " ")
  sentence = sentence.replace('.', ' ')
  return sorted([word.lower() for word in sentence.split()],  key = lambda word:len(word))[-1]

