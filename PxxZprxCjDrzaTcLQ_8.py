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
  import re
  lst=txt.split(' ')
  for i in range(len(lst)-1):
    if re.search("[aeiou]",lst[i][-1])and re.search("[aeiou]",lst[i+1][0]):
      return True
  return False

