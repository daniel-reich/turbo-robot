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
    pass
​
  def run(self, instructions):
    s = [0]
    for x in instructions.split():
      if x.isdigit():
        s.append(int(x))
      elif x == '+':
        s.append(s.pop() + s.pop())
      elif x == '-':
        s.append(s.pop() - s.pop())
      elif x == '*':
        s.append(s.pop() * s.pop())
      elif x == '/':
        s.append(s.pop() / s.pop())
      elif x == 'DUP':
        x = s.pop()
        s.append(x)
        s.append(x)
      elif x == 'POP':
        s.pop()
      else:
        self.value = 'Invalid instruction: ' + x
        return
    self.value = s.pop()
​
  def getValue(self):
    return self.value

