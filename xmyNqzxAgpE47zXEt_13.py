"""


A word is alphabetically sorted if all of the letters in it are in consecutive
alphabetical order. Some examples of alphabetically sorted words: _abhors_ (
_a_ is before _b_ , _b_ is before _h_ , _h_ is before _o_ , etc.), _ghost_ ,
_accent_ , _hoop_.

Create a function that takes in a sentence as input and returns `True` if
there is **at least one** alphabetically sorted word inside that has a
**minimum length of 3**.

### Examples

    is_alphabetically_sorted("Paula has a French accent.") ➞ True
    # "accent" is alphabetically sorted.
    
    is_alphabetically_sorted("The biopsy returned negative results.") ➞ True
    # "biopsy" is alphabetically sorted.
    
    is_alphabetically_sorted("She sells sea shells by the sea shore.") ➞ False
    # Although "by" is alphabetically sorted, it is only 2 letters long.

### Notes

  * Do not count words with 2 or fewer characters.
  * Ignore punctuation (periods, commas, etc).

"""

def is_alphabetically_sorted(txt):
    import string
    txt_clean = txt.translate(str.maketrans('', '', string.punctuation)).split(" ")
    sorted_txt = ["".join(sorted(txt_clean[i])) for i in range(0,len(txt_clean))]
    txt_compare = [sorted_txt[i] == txt_clean[i] and len(txt_clean[i])>=3 for i in range(0,len(sorted_txt))]
    return any(txt_compare)

