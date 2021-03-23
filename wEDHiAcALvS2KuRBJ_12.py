"""


A stack machine processes instructions by pushing and popping values to an
internal stack.  
A simple example of this is a calculator.

The argument passed to `run(instructions)` will always be a string containing
a series of instructions.  
The instruction set of the calculator will be this:

  * `+`: Pop the last 2 values from the stack, add them, and push the result onto the stack.
  * `-`: Pop the last 2 values from the stack, subtract the lower one from the topmost one, and push the result.
  * `*`: Pop the last 2 values, multiply, and push the result.
  * `/`: Pop the last 2 values, divide the topmost one by the lower one, and push the result.
  * `DUP`: Duplicate (not double) the top value on the stack.
  * `POP`: Pop the last value from the stack and discard it.
  * `PSH`: Performed whenever a number appears as an instruction. Push the number to the stack.
  * Any other instruction (for example, a letter) should result in the value "Invalid instruction: [instruction]"

### Examples

    "" ➞ 0
    
    "5 6 +" ➞ 11
    
    "3 DUP +" ➞ 6
    
    "6 5 5 7 * - /" ➞ 5
    
    "x y +" ➞ Invalid instruction: x

### Notes

  * If there are no instructions, the value should remain 0.
  * The return value of `getValue()` should be the topmost value on the stack.

"""

class StackCalc:
​
    def __init__(self):
      self.stack = []
    def run(self, instructions):
      if instructions == '':
        return
      if ' ' not in instructions:
        if instructions.isdigit():
          self.stack.append(int(instructions))
        else:
          self.stack.append(instructions)
      else:
        intsts = instructions.split(' ')
        for i in intsts:
          if i.isdigit():
            self.stack.append(int(i))
          elif i == '+' and len(self.stack)>=2:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a+b)
          elif i == '-' and len(self.stack)>=2:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a-b)
          elif i == '*' and len(self.stack)>=2:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a*b)
          elif i == '/' and len(self.stack)>=2:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a/b)
          elif i == 'DUP' and len(self.stack)>=1:
            self.stack.append(self.stack[-1])
          elif i == 'POP' and len(self.stack)>=1:
            self.stack = self.stack[:-1]
          else:
            self.stack.append(i)
            return
    def getValue(self):
      if len(self.stack)>=1:
        if type(self.stack[-1]) == type('a'):
          return 'Invalid instruction: ' + self.stack[-1]
        a = self.stack.pop()
        return a
      else:
        return 0

