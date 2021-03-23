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
    return ' '.join([f(word) for word in txt.split()])
​
def f(w):
    x = w.rfind('nts')
    y = w.rfind('nce')
    if x == y == -1:
        return w
    if x > y:
        return plug(w, x, 'nce')
    else:
        return plug(w, y, 'nts')
​
def plug(w, i, s):
    for v in w[i+3:]:
        if v.isalpha():
            return w
    return w[:i] + s + w[i+3:]

