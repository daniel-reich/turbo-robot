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
  instr_set = set(["+","-","*","/","DUP","POP"])
  def __init__(self):
    self.stack = []
    
  def run(self, instructions):
    instr = instructions.split()
    if(len(instr) == 0): return
    i = 0
    while(i < len(instr)):
      if(instr[i].isdigit()):
        self.stack.append(int(instr[i]))
      if(not instr[i].isdigit() and instr[i] not in self.instr_set): 
        self.stack.append('Invalid instruction: {}'.format(instr[i]))
        return
      if(instr[i] == '+'):
        a ,b = self.stack.pop(),self.stack.pop()
        self.stack.append(a+b)
      if(instr[i] == '-'):
        a ,b = self.stack.pop(),self.stack.pop()
        self.stack.append(a-b)
      if(instr[i] == "*"):
        a ,b = self.stack.pop(),self.stack.pop()
        self.stack.append(a*b)
      if(instr[i] == "/"):
        a ,b = self.stack.pop(),self.stack.pop()
        self.stack.append(a/b)
      if(instr[i] == "DUP"):
        self.stack.append(self.stack[-1])
      if(instr[i] == 'POP'):
        self.stack.pop()
      i += 1
  def getValue(self):
    return 0 if len(self.stack) == 0 else self.stack.pop()
    
machine = StackCalc()
machine.run("1 2 +")
print(machine.getValue())

