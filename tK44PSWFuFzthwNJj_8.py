"""


A night club will give you a word. For entrance, you need to provide the right
number according to the provided word.

Every given word will have a doubled letter, like "dd" in addiction. To answer
the right number you need to find the doubled letter's position in the
alphabets and multiply this number with 4.

Create a function that takes the argument of `word` and returns the right
number.

### Examples

    club_entry("hill") ➞ 48
    # 'l' is 12th alphabet
    # 12*4 = 48
    
    club_entry("apple") ➞ 64
    
    club_entry("bee") ➞ 20

### Notes

N/A

"""

def club_entry(word):
  alphabet=[]
  password=0
  for i in range(97,123):
    alphabet.append(chr(i))
  for y in range(0,len(word)-1):
    if word[y]==word[y+1]:
      password+=(alphabet.index(word[y])+1)*4
  return password

