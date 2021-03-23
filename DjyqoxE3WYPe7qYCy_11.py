"""


Given a string, reverse all the words which have odd length. The even length
words are not changed.

### Examples

    reverse_odd("Bananas") ➞ "sananaB"
    
    reverse_odd("One two three four") ➞ "enO owt eerht four"
    
    reverse_odd("Make sure uoy only esrever sdrow of ddo length")
    ➞ "Make sure you only reverse words of odd length"

### Notes

There is exactly one space between each word and no punctuation is used.

"""

def reverse_odd(txt):
  if(txt == ""):
    return txt
  else:
    ss = list(txt.strip().split(' '))
    ret = ""
    for i in range(0,len(ss)):
      k = list(ss[i].strip())
      if(len(k)%2 == 0):
        ret += ss[i]
      else:
        k = k[::-1]
        for p in k:
          ret += str(p)
      if(i != (len(ss)-1)):
        ret += " "
    return ret

