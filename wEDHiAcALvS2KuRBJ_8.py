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
  def __init__(self):
    self._stack = [0]
    self._valid = {
      "+": self._add,
      "-": self._sub,
      "*": self._mul,
      "/": self._div,
      "DUP": self._dup,
      "POP": self._pop,
    }
  def _add(self):
    x, y = self._stack.pop(), self._stack.pop()
    self._stack.append(x.__add__(y))
  def _sub(self):
    x, y = self._stack.pop(), self._stack.pop()
    self._stack.append(x.__sub__(y))
  def _mul(self):
    x, y = self._stack.pop(), self._stack.pop()
    self._stack.append(x.__mul__(y))
  def _div(self):
    x, y = self._stack.pop(), self._stack.pop()
    self._stack.append(x.__floordiv__(y))
  def _dup(self):
    x = self._stack.pop()
    self._stack.append(x)
    self._stack.append(x)
  def _pop(self):
    self._stack.pop()
  def run(self, instructions):
    for inst in instructions.split(" "):
      try:
        self._stack.append(int(inst))
      except ValueError:
        if inst in self._valid:
          self._valid[inst]()
        elif inst == "":
          self._stack = [0]
          break
        else:
          self._stack = ["Invalid instruction: {}".format(inst)]
          break
  def getValue(self):
    return self._stack.pop()

