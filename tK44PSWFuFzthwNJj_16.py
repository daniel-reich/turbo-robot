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
  i = 0
  x = len(word)
  if word[i] == word[1+i]:
    y =((ord(word[i])-96)*4)
  else:
    while i < x:
      if word[i] == word[1+i]:
        break
      i+=1
      y =((ord(word[i])-96)*4)
  return(y)

