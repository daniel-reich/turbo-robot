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
    c=[]
    a=txt.split('.')
    b=''
    if a[-1]=='':
        for i in a[:-2]:
            b+=(i.lower())
        for i in a[-2]:
            c.append(i)
        if ' '.join(c[1:])==b.capitalize():
            return True
        else:
            return False
    else:
        for i in a[:-1]:
            b+=(i.lower())
        for i in a[-1][:-1]:
            c.append(i)
        if ' '.join(c[1:])==b.capitalize():
            return True
        else:
            return False

