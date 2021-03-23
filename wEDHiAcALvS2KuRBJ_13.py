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
    self.stack = [0]
    self._instructions_1 = ['DUP', 'POP']
    self._instructions_2 = ['+', '-', '*', '/']
​
  def run(self, instructions):
    for instruction in instructions.split():
    
      if instruction.isdigit():
        self.stack.append(int(instruction))
        continue
        
      if instruction in self._instructions_1:
        if len(self.stack) < 1:
          self.stack = ['Empty set encountered.']
          break
        elif instruction == 'DUP':
          self.stack.append(self.stack[-1])
        elif instruction == 'POP':
          self.stack.pop()
        continue
        
      if instruction in self._instructions_2:
        if len(self.stack) < 2:
          self.stack = ['Not enough elements in stack.']
          break
        a, b = self.stack.pop(), self.stack.pop()
        if instruction == '+':
          self.stack.append(a + b)
        elif instruction == '-':
          self.stack.append(a - b)
        elif instruction == '*':
          self.stack.append(a * b)
        elif instruction == '/':
          self.stack.append(a / b)
        continue
        
      if instruction != '': 
        self.stack = ["Invalid instruction: {}".format(instruction)]
        break
      
  def getValue(self):
    return self.stack[-1] if len(self.stack) > 0 else None

