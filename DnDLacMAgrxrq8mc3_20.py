"""


Create a function which replaces the last `n` words with "blah". Add `"..."`
to the last blah.

### Examples

    blah_blah("A function is a block of code which only runs when it is called",  5) ➞ "A function is a block of code which only blah blah blah blah blah..."
    
    blah_blah("one two three four five", 2) ➞ "one two three blah blah..."
    
    blah_blah("Sphinx of black quartz judge my vow", 10) ➞ "blah blah blah blah blah blah blah..."

### Notes

  * If `n` is longer than the amount of words in the sentence, replace every word with "blah" (see example #3).
  * All blahs shall be lowercase!

"""

def blah_blah(txt, n):
  u = txt.split(' ')[::-1]
  for i in range(min(n, len(u))):
    u[i] = 'blah'
  return ' '.join(u[::-1]) + '...'

