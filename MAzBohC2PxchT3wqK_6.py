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
    lst_a, lst_b = a.split(), b.split()
    if len(lst_a) == len(lst_b):
        for x, y in zip(lst_a, lst_b):
            if len(x) != len(y) or set(x) & set(y):
                return False
        return True
    return False

