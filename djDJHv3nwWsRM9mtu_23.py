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
  
  raw = txt.split()
  
  word = raw[-1]
  l8rs = []
  
  for l8r in raw[:-1]:
    for item in l8r:
      if item != '.':
        l8rs.append(item)
  
  word = list(word.upper().strip('?').strip('!').strip('.')) 
  
  return word == l8rs

