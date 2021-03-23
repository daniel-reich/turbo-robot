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

def find_longest(s, mword=""):
  if len(s) == 0:
    if '\'' in mword: 
      mword = mword.split('\'')[0].lower()
    return "".join([c for c in mword if c.isalpha()]).lower()
​
  if len(s.split()[0]) > len(mword):
    mword = s.split()[0]
  
  return find_longest(" ".join(s.split()[1:]), mword)

