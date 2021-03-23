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
    self.inp_parsed = []
    self.invalid = False
  def run(self, instructions):
    inp_parsed = instructions.split(" ")
    for el in inp_parsed:
      if el.isnumeric():
        self.stack.append(int(el))
      elif el in ["+", "-", "*", "/"]:
        num1 = self.stack.pop()
        num2 = self.stack.pop()
        if el == "+":
          self.stack.append(num1 + num2)
        elif el == "-":
          self.stack.append(num1 - num2)
        elif el == "*":
          self.stack.append(num1 * num2)
        else:
          self.stack.append(num1 / num2)
      elif el == "DUP":
        self.stack.append(self.stack[-1])
      elif el == "POP":
        if self.stack:
          self.stack.pop()
      elif el.isalpha():
        self.stack = [el]
        self.invalid = True
        break
        
  def getValue(self):
    if self.stack:
      if self.invalid:
        return "Invalid instruction: {}".format(self.stack[0])
      return self.stack.pop()
    return 0

