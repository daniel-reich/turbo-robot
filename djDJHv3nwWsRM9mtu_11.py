"""


Given a sentence spelling out a word, return `True` if the spelled letters
match the _word at the end of the string_.

### Examples

    validate_spelling("C. Y. T. O. P. L. A. S. M. Cytoplasm?") ➞ True
    
    validate_spelling("P. H. A. R. A. O. H. Pharaoh!") ➞ True
    
    validate_spelling("H. A. N. K. E. R. C. H. E. I. F. Handkerchief.") ➞ False

### Notes

  * The word at the end is **always spelled correctly**.
  * Spelled words will always end in punctuation (but ignore all punctuation).

"""

def validate_spelling(txt):
  return ''.join(l[0] for l in txt.split()[:-1])==txt.split()[-1][:-1].upper()

