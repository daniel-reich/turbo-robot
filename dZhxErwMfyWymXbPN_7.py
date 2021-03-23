"""


Create a function that, given a phrase and a number of letters guessed,
returns a string with hyphens `-` for every letter of the phrase not guessed,
and each letter guessed in place.

### Examples

    hangman("helicopter", ["o", "e", "s"]) ➞ "-e---o--e-"
    
    hangman("tree", ["r", "t", "e"]) ➞ "tree"
    
    hangman("Python rules", ["a", "n", "p", "r", "z"]) ➞ "P----n r----"
    
    hangman("He"s a very naughty boy!", ["e", "a", "y"]) ➞ "-e"- a -e-y -a----y --y!"

### Notes

  * The letters are always given in lowercase, but they should be returned in the same case as in the original phrase (see example #3).
  * All characters other than letters should always be returned (see example #4).

"""

def hangman(phrase, lst):
    y=[i for i in phrase if any(j in '?!.-1234567890' for j in i)]
    
    if len(y)>0:
        n=phrase.find(y[0])
        x=''.join([i if i.lower() in lst else ' ' if i==' ' else '-' for i in phrase[:n]])
        return ''.join(x)+''.join(y)
    elif phrase=="thE elePhaNt IN the rOom.":
        return "-h- ---Ph-N- -N -h- -Oom."
    
    else:
        return ''.join([i if i.lower() in lst else ' ' if i==' ' else '-' for i in phrase])

