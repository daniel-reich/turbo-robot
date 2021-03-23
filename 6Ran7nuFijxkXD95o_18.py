"""


Given a sentence containing few instances of `"Ctrl + C"` and `"Ctrl + V"`,
return the sentence after those keyboard shortcuts have been applied! Note
that:

  * In this case, `"Ctrl + C"` will copy **all text** behind it.
  * In this case, `"Ctrl + V"` will do nothing if there is no `"Ctrl + C"` before it.
  * A `"Ctrl + C"` which follows another `"Ctrl + C"` will overwrite what it copies.

### Examples

    keyboard_shortcut("the egg and Ctrl + C Ctrl + V the spoon") ➞ "the egg and the egg and the spoon"
    
    keyboard_shortcut("WARNING Ctrl + V Ctrl + C Ctrl + V") ➞ "WARNING WARNING"
    
    keyboard_shortcut("The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V") ➞ "The The Town The The Town"

### Notes

  * Keyboard shortcut commands will appear like normal words in a sentence but shouldn't be copied themselves (see example #2).
  * Pasting should add a space between words.

"""

def keyboard_shortcut(txt):
  def formatter_fix(txt):
​
    words = txt.split()
​
    return ' '.join(words)
​
  txt = txt.replace('Ctrl + C', '<').replace('Ctrl + V', '>')
​
  class Formatter:
​
    def __init__(self, txt = '', stack = ''):
      self.t = txt
      self.stack = stack
    
    def read(self, txt):
      txt = list(txt)
​
      for n in range(len(txt)):
        try:
          item = txt[n]
        except IndexError:
          break
        if item == '<':
          self.stack = ''.join(self.t)
        elif item == '>':
          if len(self.stack) > 0:
            self.t += self.stack
            self.stack = '' 
          else:
            txt.pop(n)         
        else:
          self.t += item
      return True
  
  f = Formatter()
​
  f.read(txt)
​
  return formatter_fix(f.t)

