"""


Write a function that takes a string, and returns a new string with any
duplicate _consecutive_ letters removed.

### Examples

    unstretch("ppoeemm") ➞ "poem"
    
    unstretch("wiiiinnnnd") ➞ "wind"
    
    unstretch("ttiiitllleeee") ➞ "title"
    
    unstretch("cccccaaarrrbbonnnnn") ➞ "carbon"

### Notes

Final strings _won't_ include words with double letters (e.g. "passing",
"lottery").

"""

def unstretch(word):
  new_word = ''
  last_letter = ''
  for letter in word:
    if letter != last_letter:
      new_word += letter
      last_letter = letter
  return new_word

