"""


A local news station needs your help to generate the scrolling text for the
headlines!

Create a function that returns a list of strings, where each string contains a
single frame of what the scrolling text will look like.

  * Text will scroll from right to left.
  * The screen will have a width of `n` characters.
  * Start and stop when no letters appear on the screen.

The example below will demonstrate the output when the screen width is **10**.

### Examples

    news_at_ten("edabit", 10) ➞ [
      "          ",
      "         e",
      "        ed",
      "       eda",
      "      edab",
      "     edabi",
      "    edabit",
      "   edabit ",
      "  edabit  ",
      " edabit   ",
      "edabit    ",
      "dabit     ",
      "abit      ",
      "bit       ",
      "it        ",
      "t         ",
      "          "
    ]

### Notes

  * Every string should be `n` characters long, so you should pad the string with spaces if the text isn't long enough.
  * Similarly, if the text is too long for the screen width, then it's only possible to display a fraction of the text at a time.
  * See the **Tests** tab for more examples.

"""

from itertools import count
​
def news_at_ten(txt, n):
    pad = ' ' * n
    txt = pad + txt + pad
​
    result = [txt[0:n]]
​
    counter = count(1)
    while True:
        start = next(counter)
        end = start + n
        result.append(txt[start:end])
        if result[-1] == ' ' * n:
            break
​
    return result

