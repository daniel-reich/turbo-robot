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

import re
find_longest=lambda s,recur=0: find_longest(re.split(r"\W",s),1) if recur==0 else s[0].lower() if len(s)==1 else find_longest(s[1:],1) if len(s[0])<len(s[1]) else find_longest([s[0]]+s[2:],1)

