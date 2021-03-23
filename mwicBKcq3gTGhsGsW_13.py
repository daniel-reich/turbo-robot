"""


What does the word **LFAND** represent? It represents the word **Finland** ,
because F is _in_ LAND!

Create a function which replicates this to create brand new original word
riddles! For the purposes of this challenge, take the string of letters
_before the word "in"_ , and insert it into the **2nd letter position** of the
word formed _after the word "in"_.

See the examples below for further clarity :)

### Examples

    make_word_riddle("Finland") ➞ "LFAND"
    
    make_word_riddle("dinner") ➞ "NDER"
    
    make_word_riddle("tkinter") ➞ "TTKER"
    
    make_word_riddle("STRINGS") ➞ "GSTRS"

### Notes

  * All words given will contain only one occurence of "in" (so no occurences of the words _Insulin_ , _Infinity_ , etc).
  * There will be no examples of _Interest_ , _Pin_ , or _Ping_ , etc... as there is no clear way to insert the strings into one another.
  * Return in all **CAPS**.

"""

def make_word_riddle(s):
  a,b = s.upper().split("IN")
  return b[0]+a+b[1:]

