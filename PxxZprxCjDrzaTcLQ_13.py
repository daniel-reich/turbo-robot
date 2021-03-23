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

def vowel_links(string):
  lst = string.split()
  vowels = ['a', 'e', 'i', 'o', 'u']
  for i in range(len(lst)):
    if i != len(lst)-1:
      print(i, lst[i][len(lst[i])-1], lst[i+1][0])
      if (lst[i][len(lst[i])-1] in vowels) and (lst[i+1][0] in vowels):
        return True
  return False

