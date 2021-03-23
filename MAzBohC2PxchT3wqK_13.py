"""


Given two sentences, return whether they are shadows of each other. This means
that all of the word lengths are the same, but the corresponding words don't
share any common letters.

### Examples

    shadow_sentence("they are round", "fold two times") ➞ True
    
    shadow_sentence("own a boat", "buy my wine") ➞ False
    # No words share common letters, but "a" and "my" have different lengths.
    
    shadow_sentence("his friends", "our company") ➞ False
    # Word lengths are the same but "friends" and "company" share the letter "n".
    
    shadow_sentence("salmonella supper", "birthright") ➞ False
    # Setences with different numbers of words.

### Notes

  * All sentences will be given in lowercase, and will have no punctuation.
  * Return `False` if the sentences have different numbers of words.

"""

def shadow_sentence(a, b):
  alist, blist = a.split(' '), b.split(' ')
  if len(alist) != len(blist):
    return False
  
  j = -1
  for word in alist:
    j += 1
    if len(word) != len(blist[j]):
      return False
  
  i = -1
  for word in blist:
    i += 1
    for letter in word:
      if letter in alist[i]:
        return False
        
  return True

