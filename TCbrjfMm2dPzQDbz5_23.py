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
  pos = []
  for idx, c in enumerate(txt):
    if c.isupper():
      pos += [idx]
  pos += [len(txt)]
  return ' '.join(txt[pos[i]: pos[i + 1]] for i in range(len(pos) - 1))

