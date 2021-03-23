"""


Create a function which takes every letter in every word, and puts it in
alphabetical order. Note how the **original word lengths must stay the same**.

### Examples

    true_alphabetic("hello world") ➞ "dehll loorw"
    
    true_alphabetic("edabit is awesome") ➞ "aabdee ei imosstw"
    
    true_alphabetic("have a nice day") ➞ "aaac d eehi nvy"

### Notes

  * All sentences will be in lowercase.
  * No punctuation or numbers will be included in the **Tests**.

"""

def true_alphabetic(txt):
  ch, length, alph = sorted(i for i in txt if i.isalpha()), [len(i) for i in txt.split()], []
  for i in length:
    alph.append(''.join(ch[:i]))
    ch = ch[i:]
  return ' '.join(alph)

