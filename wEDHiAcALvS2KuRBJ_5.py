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

instruction_dict = {"+": "s = sum(self.stack[-2:])\ndel self.stack[-2:]\nself.stack.append(s)",
                    "-": "s = [self.stack[-1], self.stack[-2]]\ndel self.stack[-2:]\nself.stack.append(max(s) - min(s))",
                    "*": "s = self.stack[-1] * self.stack[-2]\ndel self.stack[-2:]\nself.stack.append(s)",
                    "/": "s = [self.stack[-1], self.stack[-2]]\ndel self.stack[-2:]\nself.stack.append(max(s) // min(s))",
                    "DUP": "s = self.stack[-1]\nself.stack.insert(-1, s)",
                    "POP": "del self.stack[-1]"}
​
class StackCalc:
    def __init__(self):
        self.stack = []
        self.exception = ""
​
    def run(self, instruction):
        instruction = instruction.split()
​
        if instruction:
            if len(instruction) == 1 and instruction[0].isdigit():
                self.stack.append(int(instruction[0]))
                return
​
            for i in instruction:
                if i.isdigit():
                    self.stack.append(int(i))
                elif i in instruction_dict.keys():
                    exec(instruction_dict[i])
                else:
                    self.stack = []
                    self.exception = "Invalid instruction: {}".format(i)
                    break
​
    def getValue(self):
        if self.exception:
            return self.exception
        elif self.stack:
            return self.stack[-1]
        else:
            return 0

