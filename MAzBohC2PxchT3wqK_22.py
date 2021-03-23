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

def shadow_sentence(a,b):
    '''
    Returns whether sentence a has same number and length of each word as b, and
    also has no letters in common between corresponding words.
    '''
    a, b = a.split(), b.split()
    
    return len(a) == len(b) and all(len(w1)==len(w2) \
            and all(l not in set(w2) for l in set(w1)) for w1,w2 in zip(a,b))

