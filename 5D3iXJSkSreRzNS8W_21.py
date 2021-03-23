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

def news_at_ten(txt, n):
    lst = []
    a = n + (len(txt) * 2) - len(txt)
    for i in range(len(txt) + n + 1):
        screen = ""
        e = 0
        for i in range(n + (len(txt) * 2) + 1):
            if i != a:
                screen += " "
            elif e < len(txt):
                screen += txt[e]
                e += 1
                a += 1
        lst.append(screen[len(txt):(len(txt) + n)])
        a -= (1 + e)
    return lst

