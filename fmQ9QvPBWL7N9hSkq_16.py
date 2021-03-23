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
  lis = []
  j=0
  for i in range(len(word)):
    if i <= (len(word)-2):
      if word[i]!=word[i+1]:
        lis.append(set(word[j:i+1]))
        j = i+1
      else:
        pass
    else:
      lis.append(set(word[j:]))
  lis = [x for i in lis for x in i]
  return "".join(lis)

