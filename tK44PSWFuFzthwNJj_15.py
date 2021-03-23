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
  return 4 * (ord([word[x] for x in range(len(word)) if word[x] == word[x-1]][0]) - 96)

