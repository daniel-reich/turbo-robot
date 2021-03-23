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
  l = txt.split(' ')
  myans = []
  v = ['a','e','i','o','u']
  for i in range(len(l)):
    if l[i][0].lower() in v:
      if i > 0:
        myans.append('eek')
      else:
        myans.append('Eek')
    else:
      if i > 0:
        myans.append('ook')
      else:
        myans.append('Ook')
  return ' '.join(myans)+'.'

