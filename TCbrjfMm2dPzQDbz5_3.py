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

import re
insert_whitespace=lambda t:re.sub(r'([a-z])([A-Z])',r'\1 \2',t)

