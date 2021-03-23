"""


Create a function that takes a list and returns a string.

  *  **0** Repeat the actual decrypted value (using like this : 014 to repeat 14 times). 
    * _Warning: When you start a repeat you can't stop it to add other numbers._
  *  **1, 2, 3, 4** = g, o, l, e
  *  **5** Corresponding to up case of letter before this.
  *  **6** Add a point to the end.
  *  **7** Change case of the first letter.
  *  **8** Reverse the string.
  *  **9** Clear the actual decrypted string.

### Examples

    num_to_google(["12213467"]) ➞ "Google."
    
    num_to_google(["12213467", "321"]) ➞ "Google.log"
    
    num_to_google(["12213467", "321", "122906"]) ➞ "Google.log"
    
    num_to_google(["15", "2502", "15", 3545]) ➞ "GOOGLE"
    
    num_to_google(["15", "2502", "15", 35, 45]) ➞ "GOOGLE"
    
    num_to_google([15, 202, 1, 3, 4]) ➞ "Google"

### Notes

N/A

"""

class Encryption:
  one, two, three, four = 'g, o, l, e'.split(', ')
  
  def __init__(self, stack = []):
    self.stack = stack
  
  def add(self, item):
    
    if isinstance(item, int) == True:
      item = str(item)
    
    if '345' in item:
      item = item.replace('345', '3545')
    
    zero_in_item = False
    num = ''
    for l8r in item:
      print(self.stack)
      if zero_in_item == False:
        if l8r in '1234':
          dic = {1: Encryption.one, 2: Encryption.two, 3: Encryption.three, 4: Encryption.four}
          self.stack.append(dic[int(l8r)])
        elif l8r == '5':
          self.stack[-1] = self.stack[-1].upper()
        elif l8r == '6':
          self.stack.append('.')
        elif l8r == '7':
          if self.stack[0].islower() == True:
            self.stack[0] = self.stack[0].upper()
          else:
            self.stack[0] = self.stack[0].lower()
        elif l8r == '8':
          if '7' not in item:
            self.stack = list(reversed(self.stack))
          else:
            if self.stack[0].islower() == True:
              self.stack[0] = self.stack[0].upper()
            else:
              self.stack[0] = self.stack[0].lower()
            self.stack = list(reversed(self.stack))
            if self.stack[0].islower() == True:
              self.stack[0] = self.stack[0].upper()
            else:
              self.stack[0] = self.stack[0].lower()
        elif l8r == '9':
          for n in range(item.index('9')):
            self.stack.pop(-1)
        elif l8r == '0':
          zero_in_item = True
          zero_index = item.index('0')
      else:
        num += l8r
    print(self.stack)
    if zero_in_item == True:
      if '9' in item:
        if zero_index - 1 == item.index('9'):
          return True
      for n in range(int(num) - 1):
        for index in range(zero_index):
          l8r = item[index]
          if l8r in '1234':
            dic = {1: Encryption.one, 2: Encryption.two, 3: Encryption.three, 4: Encryption.four}
            self.stack.append(dic[int(l8r)])
          elif l8r == '5':
            self.stack[-1] = self.stack[-1].upper()
          elif l8r == '6':
            self.stack.append('.')
          elif l8r == '7':
            if self.stack[0].islower() == True:
              self.stack[0] = self.stack[0].upper()
            else:
              self.stack[0] = self.stack[0].lower()
          elif l8r == '8':
            if '7' not in item:
              self.stack = list(reversed(self.stack))
            else:
              if self.stack[0].islower() == True:
                self.stack[0] = self.stack[0].upper()
              else:
                self.stack[0] = self.stack[0].lower()
              self.stack = list(reversed(self.stack))
              if self.stack[0].islower() == True:
                self.stack[0] = self.stack[0].upper()
              else:
                self.stack[0] = self.stack[0].lower()
          elif l8r == '9':
            for n in range(item.index('9')):
              self.stack
    
    return True
  
  def display(self):
    return ''.join(self.stack)
    
def num_to_google(arr):
  
  e = Encryption([])
  
  for item in arr:
    e.add(item)
  
  return e.display()

