"""


Write a function that reverses all the words in a sentence that start with a
particular letter.

### Examples

    special_reverse("word searches are super fun", "s")
    ➞ "word sehcraes are repus fun"
    
    special_reverse("first man to walk on the moon", "m")
    ➞ "first nam to walk on the noom"
    
    special_reverse("peter piper picked pickled peppers", "p")
    ➞ "retep repip dekcip delkcip sreppep"

### Notes

  * Reverse the words themselves, not the entire sentence.
  * All characters in the sentence will be in lower case.

"""

def special_reverse(s, c):
  wordlist = s.split(' ')
  newwords = []
  for word in wordlist:
    if word[0] != c:
      newwords.append(word)
    else:
      newwords.append(word[::-1])
  return (' ').join(newwords)

