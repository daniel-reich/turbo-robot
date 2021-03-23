"""


A word is alphabetically sorted if all of the letters in it are in consecutive
alphabetical order. Some examples of alphabetically sorted words: _abhors_ (
_a_ is before _b_ , _b_ is before _h_ , _h_ is before _o_ , etc.), _ghost_ ,
_accent_ , _hoop_.

Create a function that takes in a sentence as input and returns `True` if
there is **at least one** alphabetically sorted word inside that has a
**minimum length of 3**.

### Examples

    is_alphabetically_sorted("Paula has a French accent.") ➞ True
    # "accent" is alphabetically sorted.
    
    is_alphabetically_sorted("The biopsy returned negative results.") ➞ True
    # "biopsy" is alphabetically sorted.
    
    is_alphabetically_sorted("She sells sea shells by the sea shore.") ➞ False
    # Although "by" is alphabetically sorted, it is only 2 letters long.

### Notes

  * Do not count words with 2 or fewer characters.
  * Ignore punctuation (periods, commas, etc).

"""

def is_alphabetically_sorted(sentence):
  s=sentence.replace('.', '')
  s=s.split(' ')
  lst=[]
  string=''
  one=s[0]
  two=s[1]
  three=s[2]
  try:
    four=s[3]
  except:
    four='' 
  try:
    five=s[4]
  except:
    five=''
  try:
    six=s[5]
  except:
    six=''
  try:
    seven=s[6]
  except:
    seven=''
  try:
    eight=s[7]
  except:
    eight=''
  try:
    nine=s[8]
  except:
    nine=''
  try:
    ten=s[9]
  except:
    ten=''
  one=one.lower()
  two=two.lower()
  three=three.lower()
  four=four.lower()
  five=five.lower()
  six=six.lower()
  seven=seven.lower()
  eight=eight.lower()
  nine=nine.lower()
  ten=ten.lower()
  for i in one:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==one and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in two:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==two and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in three:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==three and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in four:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==four and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in five:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==five and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in six:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==six and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in seven:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==seven and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in eight:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==eight and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in nine:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==nine and len(string) > 2):
    return True
  string=''
  lst=[]
  for i in ten:
    lst.append(i)
    lst.sort()
  for j in lst:
    string+=j
  if(string==ten and len(string) > 2):
    return True
  string=''
  lst=[]
  return False

