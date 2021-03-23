"""


Write a function that inserts a white space between every instance of a lower
character followed immediately by an upper character.

### Examples

    insert_whitespace("SheWalksToTheBeach") ➞ "She Walks To The Beach"
    
    insert_whitespace("MarvinTalksTooMuch") ➞ "Marvin Talks Too Much"
    
    insert_whitespace("TheGreatestUpsetInHistory") ➞ "The Greatest Upset In History"

### Notes

Each word in the phrase will be at least two characters long.

"""

def insert_whitespace(txt):
  ans=''
  for i in range(len(txt)-1):
    if txt[i].islower() and txt[i+1].isupper():
      ans+=txt[i]+' '
    else:
      ans+=txt[i]
  ans += txt[-1]
  return ans

