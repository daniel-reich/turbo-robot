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
  m = ''
  for i in range(len(word)-1):
    if word[i]!=word[i+1]:
      m+=word[i]
  return m+word[-1]

