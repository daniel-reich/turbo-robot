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
        self.s = []
        self.err = False
​
    def run(self, instructions):
        for i in instructions.split():
            if not self.err:
                if i.isdigit():
                    self.s += [int(i)]
                elif i == '+':
                    self.s += [self.s.pop() + self.s.pop()]
                elif i == '-':
                    self.s += [self.s.pop() - self.s.pop()]
                elif i == '*':
                    self.s += [self.s.pop() * self.s.pop()]
                elif i == '/':
                    self.s += [int(self.s.pop() / self.s.pop())]
                elif i == 'DUP':
                    self.s += [self.s[-1]]
                elif i == 'POP':
                    self.s.pop()
                else:
                    self.ret = 'Invalid instruction: '+i
                    self.err = True
​
    def getValue(self):
        if self.err:
            return self.ret
        if not self.s:
            return 0
        return self.s[-1]

