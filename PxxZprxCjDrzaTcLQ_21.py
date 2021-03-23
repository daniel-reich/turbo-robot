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
  t=txt.split()
  v="aeiou"
  for i,w in enumerate(t[:-1]):
    if w[-1] in v and t[i+1][0] in v:
      return True
  return False

