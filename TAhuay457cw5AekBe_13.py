"""


 **Mubashir** can talk with monkeys. You can also learn their simple language.

Create a function that takes a string `txt` and returns the string in
**monkeys language**. You have to figure out their language from test cases.

### Examples

    monkey_talk("Mubashir Hassan") ➞ "Ook ook."
    
    monkey_talk("Hello") ➞ "Ook."
    
    monkey_talk("Matt") ➞ "Ook."
    
    monkey_talk("Everyone") ➞ "Eek."
    
    monkey_talk("Edabit is Amazing") ➞ "Eek eek eek."

### Notes

A hint in the comments section.

"""

def monkey_talk(txt):
  def monkify(words):
    tr = []
    for word in words:
      if word[0] in 'aeiouAEIOU':
        tr.append('eek')
      else:
        tr.append('ook')
    return ' '.join(tr)
  
  return monkify(txt.split()).capitalize() + '.'

