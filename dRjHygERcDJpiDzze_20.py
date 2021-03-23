"""


Write a function that repeats the shorter string until it is equal to the
length of the longer string.

### Examples

    lengthen("abcdefg", "ab") ➞ "abababa"
    
    lengthen("ingenius", "forest") ➞ "forestfo"
    
    lengthen("clap", "skipping") ➞ "clapclap"

### Notes

  * Both strings will differ in length.
  * Both strings will contain at least one character.
  * Either of the two strings could be the shortest in length.

"""

def lengthen(s1, s2):
  lst= [len(s1),len(s2)]
  num = max(lst)//min(lst)
  part= max(lst)%min(lst)
  if len(s1) > len(s2) :compaunder = s2
  elif  len(s1) <  len(s2) :compaunder = s1
  else: compaunder = ''
  result=''
  for i in range(num):
    result = result +compaunder
  result = result + compaunder[:part]
  return result

