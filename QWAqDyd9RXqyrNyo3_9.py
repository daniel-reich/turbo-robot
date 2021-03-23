"""


Create a function which takes a `sentence` and returns its abbreviation. Get
all of the words over or equal to `n` characters in length and return the
first letter of each, _capitalised_ and overall returned as a single string.

### Examples

    abbreviate("do it yourself") ➞ "Y"
    
    abbreviate("do it yourself", 2) ➞ "DIY"
    # "do" and "it" are included because the second parameter specified that word lengths 2 are allowed.
    
    abbreviate("attention AND deficit OR hyperactivity THE disorder") ➞ "ADHD"
    # Words below the default 4 characters are not included in the abbreviation.
    
    abbreviate("the acronym of long word lengths", 5) ➞ "AL"
    # "acronym" and "lengths" have 5 or more characters.

### Notes

There may not be an argument given for `n` so set the default to `4`.

"""

def abbreviate(sentence, n=4):#w/o built-in
  def length(s):
    count = 0
    while s != "":
      count += 1
      s = s[1:]
    return count
  se, tmp = [], ""
  for i in sentence:
    if i == " ":
      se += [tmp]
      tmp = ""
    else:
      tmp += i
  if tmp:
    se += [tmp]
  to_abb = [x[0] for x in se if length(x) >= n]
  to_upper = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F',
  'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L',
  'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R',
  's': 'S', 't': 'T', 'u': 'U', 'v': 'V', 'w': 'W', 'x': 'X',
  'y': 'Y', 'z': 'Z'}
  abbreviated = ""
  for i in to_abb:
    abbreviated += to_upper[i]
  return abbreviated
​
def abbreviate(sentence, n=4): #w/ built-in
  return ''.join(i[0].upper() for i in sentence.split() if len(i) >= n)

