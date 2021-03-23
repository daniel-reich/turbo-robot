"""


Write a **recursive** function that will return the longest word in a
sentence. In cases where more than one word is found, return the first one.

### Examples

    find_longest("I will and ever will be gratefully and perpetually loving you Tesh!") ➞ "perpetually"
    
    find_longest("A thing of beauty is a joy forever.") ➞ "forever"
    
    find_longest("Forgetfulness is by all means powerless!") ➞ "forgetfulness"
    
    find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel.") ➞ "strengths"

### Notes

  * Special characters and symbols _don't count_ as part of the word.
  * Return the longest word found in **lowercase** letters.
  * You are expected to solve this challenge via a **recursive** approach.
  * An **iterative** versions of this challenge can be found via these links ([1](https://edabit.com/challenge/Z6kRGLpYgSuFQJ7Rx) and [2](https://edabit.com/challenge/Aw2QK8vHY7Xk8Keto)).

"""

def find_longest(s):
  lens = []
  s = list(s.lower())
  for i in s:
    if s.index(i) != (len(s))-1:
        if i == """'""":
          s[s.index(i)+1] = ''
    if i not in "qwertyuiopasdfghjklzxcvbnm ":
      s[s.index(i)] = ''
  s = ''.join(s)
  x = s.split()
  for i in x:
    lens.append(len(i))
  return x[lens.index(max(lens))]

