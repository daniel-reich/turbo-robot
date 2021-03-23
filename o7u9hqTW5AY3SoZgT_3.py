"""


Create a function which **replaces** all instances of `"nts"` with `"nce"` and
**vice versa** if they are at the _end of a word_.

### Examples

    switcheroo("The elephants in France were chased by ants!") ➞ "The elephance in Frants were chased by ance!"
    
    switcheroo("While he rants, I fall into a trance...") ➞ "While he rance, I fall into a trants..."
    
    switcheroo("Bounced over the fence!") ➞ "Bounced over the fents!"

### Notes

  * Empty strings should return just an empty string (see example #2).
  * Ignore punctuation and any instances where `"nts"` or `"nce"` are not at the end of a word (see example #3).

"""

def switcheroo(txt):
  copy=''.join(i if i.isalpha() else '@' for i in txt).replace('nts@','#').replace('nce@','nts@').replace('#','nce@')
  return ''.join(copy[i] if copy[i].isalpha() else txt[i] for i in range(len(txt)))

