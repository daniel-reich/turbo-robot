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

def validate_spelling(txt): #w/o built-in
    d = {"A": "a", "B": "b", "C": "c", "D": "d", "E": "e", "F": "f",
         "G": "g", "H": "h", "I": "i", "J": "j", "K": "k", "L": "l",
         "M": "m", "N": "n", "O": "o", "P": "p", "Q": "q", "R": "r",
         "S": "s", "T": "t", "U": "u", "V": "v", "W": "w", "X": "x", "Y": "y", "Z": "z"}
    t = ""
    for i in txt:
        if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ':
            if i in d:
                t += d[i]
            else:
                t += i
    s, tmp = [], ""
    for i in t:
        if i == " ":
            s += [tmp]
            tmp = ""
        else:
            tmp += i
    if tmp:
        s += [tmp]
    same = ""
    for i in s[:-1]:
        same += i
    return same == s[-1]

