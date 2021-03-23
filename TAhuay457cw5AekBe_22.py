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
  vowels = 'aeiou'
  words = txt.split()
  output = ""
  for word in words:
    if word[0].lower() in vowels:
      output += "eek "
    else:
      output += "ook "
  output = output[0].upper()+output[1:-1]+"."
  return output

