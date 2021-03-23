"""


Create a function that takes in two words as input and returns a list of three
elements, in the following order:

  1. Shared letters between two words.
  2. Letters unique to word 1.
  3. Letters unique to word 2.

Each element should have **unique** letters, and have each letter be
**alphabetically sorted**.

### Examples

    letters("sharp", "soap") ➞ ["aps", "hr", "o"]
    
    letters("board", "bored") ➞ ["bdor", "a", "e"]
    
    letters("happiness", "envelope") ➞ ["enp", "ahis", "lov"]
    
    letters("kerfuffle", "fluffy") ➞ ["flu", "ekr", "y"]
    # Even with multiple matching letters (e.g. 3 f's), there should 
    # only exist a single "f" in your first element.
    
    letters("match", "ham") ➞ ["ahm", "ct", ""]
    # "ham" does not contain any letters that are not found already 
    # in "match".

### Notes

  * Both words will be in lower case.
  * You do not have to worry about punctuation, all words only have letters from `[a-z]`.
  * If an element contains no letters, return an empty string (see last example).

"""

def letters(word1, word2):
  w1 = set(word1)
  w2 = set(word2)
  shared = []
  w1_list = []
  w2_list = []
  for c in w1 :
    if c in w2 :
      shared.append(c)
    else :
      w1_list.append(c)
  for c in w2 :
    if c not in w1:
      w2_list.append(c)
  shared.sort()
  w1_list.sort()
  w2_list.sort()
  return [''.join(shared),''.join(w1_list), ''.join(w2_list)]

