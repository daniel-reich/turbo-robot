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
    None
​
  def run(self, instructions):
    func, ndx = True, 1
    instructions = instructions.split()
​
    if not instructions:
      instructions += '0'
    elif instructions[0].isdigit() and len(instructions) > 1:
      for i in range(len(instructions)):
        if not instructions[i].isdigit():
          ndx = i
          break
​
    self.operands = instructions[:ndx]
    self.operators = instructions[ndx:]
​
    if any(val.isalpha() for val in self.operands):
      self.operands = ['Invalid instruction: %s' % self.operands[0]]
      func = False
    else:
      self.operands = [int(x) for x in self.operands]
​
    if func:
      for op in self.operators:
        if op == '+':
          self.operands.append(self.operands.pop() + self.operands.pop())
        elif op == '-':
          self.operands.append(self.operands.pop() - self.operands.pop())
        elif op == '*':
          self.operands.append(self.operands.pop() * self.operands.pop())
        elif op == '/':
          self.operands.append(self.operands.pop() // self.operands.pop())
        elif op == 'DUP':
          self.operands.append(self.operands[-1])
        elif op == 'POP':
          self.operands.pop()
          if not self.operands:
            self.operands.append(0)
        elif op.isdigit():
          self.operands.append(int(op))
        else:
          self.operands = ['Invalid instruction: %s' % op]
​
  def getValue(self):
    return self.operands[-1]

