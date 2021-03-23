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
  test1 = lambda w1, w2: len(w1) == len(w2)
  test2 = lambda w1, w2: len([l8r for l8r in w1 if l8r in w2]) == 0
  
  a = a.split()
  b = b.split()
  
  if len(a) != len(b):
    return False
  
  for n in range(len(a)):
    aword = a[n]
    bword = b[n]
    
    t1 = test1(aword, bword)
    t2 = test2(aword, bword)
#print(t1, t2, aword, bword)
    if False in [t1, t2]:
      return False
  
  return True

