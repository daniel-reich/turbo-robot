"""


Given a sentence as `txt`, return `True` if any two adjacent words have this
property: One word ends with a vowel, while the word immediately after begins
with a vowel (a e i o u).

### Examples

    vowel_links("a very large appliance") ➞ True
    
    vowel_links("go to edabit") ➞ True
    
    vowel_links("an open fire") ➞ False
    
    vowel_links("a sudden applause") ➞ False

### Notes

You can expect sentences in only lowercase, with no punctuation.

"""

def vowel_links(txt):
  v = ['a', 'e', 'i', 'o', 'u']
  l = [word for word in txt.split(' ')] + [' ']
  vlink = lambda x: l[l.index(x)][-1] in v and l[l.index(x)+1][0] in v
  return any(vlink(w) for w in l)

