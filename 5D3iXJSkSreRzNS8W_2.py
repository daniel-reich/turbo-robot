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

class TV:
  
  def __init__(self, width):
    self.width = width
    self.line_template = ' ' * self.width
  
  def display(self, msg):
​
    tr = [self.line_template]
    print(len(self.line_template), self.width)
​
    for n in range(1, self.width + 1):
      line = self.line_template[:-n] + msg[:n]
      while len(line) < self.width:
        line += ' '
      tr.append(line)
    for n in range(1, len(msg)):
      if len(msg[n:]) < self.width:
        line = msg[n:] + self.line_template[len(msg[n:]):]
      else:
        line = msg[n:n+self.width]
      tr.append(line)
    
    tr.append(self.line_template)
​
    return tr
  
def news_at_ten(txt, n):
  
  tv = TV(n)
  return tv.display(txt)

