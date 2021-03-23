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
        self.stack = []
        self.err = ""
​
​
    def run(self, instructions):
        listInstruction = []
        if instructions == '':
            self.stack.append(0)
            return self.stack
        elif instructions[0].isdigit() == False and instructions[0] != '':
            self.err = 'Invalid instruction: ' + str(instructions[0])
            return self.err
​
        for val in instructions.split():
            if val.isdigit():
                self.stack.append(int(val))
                continue
            else:
                listInstruction = instructions[instructions.index(val):].split()
                break
​
        if len(listInstruction) == 0:
            return self.stack
        
        for i in listInstruction:
            # print(i, self.stack)
            if i == "DUP":
                self.stack.append(self.stack[-1])
                continue
            elif i == "POP":
                self.stack = self.stack[:-1] if len(self.stack)>1 else [0]
                continue
            elif i.isdigit():
                self.stack.append(int(i))
                continue
            elif i.isalpha():
                self.err = 'Invalid instruction: ' + i
                return self.err
            elif eval(str(self.stack[-1]) + i + str(self.stack[-2])) == 0:
                del self.stack[-1]
                continue
            else:
                self.stack[-1] = int(eval(str(self.stack[-1]) + i + str(self.stack[-2])))
                del self.stack[-2] 
        return self.stack
    def getValue(self):
        toreturn = self.err if len(self.err)> 0 else self.stack[-1]
        return toreturn

