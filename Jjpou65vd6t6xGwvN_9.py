"""


Create a function which returns `"upper"` if all the letters in a word are
**uppercase** , `"lower"` if **lowercase** and `"mixed"` for any mix of the
two.

### Examples

    get_case("whisper...") ➞ "lower"
    
    get_case("SHOUT!") ➞ "upper"
    
    get_case("Indoor Voice") ➞ "mixed"

### Notes

Ignore punctuation, spaces and numbers.

"""

def get_case(txt):
  sCase=""
  tmpCase=""
  cnt=0
  a=len(txt)
  for i in range(0,a):
    if(txt[i].isalpha()):
      if(txt[i].islower()):
        sCase="lower"
      else:
        sCase="upper"
      if(cnt>0):
        if(tmpCase!=sCase):
          return "mixed"
      cnt=cnt+1
      tmpCase=sCase
  return sCase

