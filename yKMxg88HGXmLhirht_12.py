"""


Create a function `add_letters` that takes a list/array of letters `a`, and
returns the "sum" of them.

To add two letters, take their number value, add them together, and convert it
back together. For example, `a` would be `1`, `b` would be `2`, etc. So to add
`b` and `c`, take `2 + 3 = 5`, and then get the fifth letter of the alphabet
(`e`).

So then `d + e + f` would be `4 + 5 + 6 = 15`, and the fifteenth letter is
`o`, so that's what you return.

Letters can also wrap. Like with `y + c`, that's `25 + 3 = 28`, which doesn't
exist. Consider that the 27th letter just wraps around and ends back up at
`a`. With this logic, `y + c = b`. Don't just do 27 = 1 though, because you
could end up with a much higher sum like 70.

### Examples

    add_letters(["a"]) ➞ "a"
    add_letters(["a", "b"]) ➞ "c"
    add_letters(["a", "b", "c"]) ➞ "f"
    add_letters(["a", "b", "c", "d", "e", "f"]) ➞ "u"
    add_letters(["y", "a"]) ➞ "z"
    add_letters(["y", "c"]) ➞ "b"
    add_letters(["z", "a"]) ➞ "a"
    add_letters(["x", "y", "z"]) ➞ "w"
    add_letters([]) ➞ "z"

### Notes

  * Don't forget to `return` the result.
  * An empty array should return `z`. The logic behind this is that if you get a sum of `0`, then wrap it all the way around backwards (since the 0th letter doesn't exist), giving you 26 which = `z`.
  * All letters given will be lowercase.

"""

def add_letters(a):
  values = {'z':0, 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8,
  'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 
  'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25}
  total = 0
  for i in a:
    total += values[i]
  total = total % 26
  for i in values:
    if values[i] == total:
      return i

