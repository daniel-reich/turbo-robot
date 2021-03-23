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
        self.tmpInstruction = list()
        self.do = True
​
    def run(self, instructions):
        if instructions == "" or instructions == []:
            self.do = False
            self.tmpInstruction = 0
            return 0
        if type(instructions) == str:
            self.tmpInstruction = [item for item in instructions.split(" ")]
​
        for item in self.tmpInstruction:
            if item == "x":
                abort = "x"
                return('Invalid instruction: {}'.format(abort))
            else:
                if item == "y":
                    abort = "y"
                    return('Invalid instruction: {}'.format(abort))
        if len(self.tmpInstruction) == 1 or all(item.isdigit() for item in self.tmpInstruction):
            self.getValue()
        else:
            while self.do == True:
                for i in range(len(self.tmpInstruction)):
                    if self.do == False:
                        break
                    if self.tmpInstruction[i].isnumeric():
                        pass
                    elif self.tmpInstruction[i] == "+":
                        self.tmpInstruction[i] = str(int(self.tmpInstruction[i-1]) + int(self.tmpInstruction[i-2]))
                        del self.tmpInstruction[i-2:i]
                        self.run(self.tmpInstruction)
                    elif self.tmpInstruction[i] == "-":
                        self.tmpInstruction[i] = str(int(self.tmpInstruction[i-1]) - int(self.tmpInstruction[i-2]))
                        del self.tmpInstruction[i-2:i]
                        self.run(self.tmpInstruction)
                    elif self.tmpInstruction[i] == "*":
                        self.tmpInstruction[i] = str(int(self.tmpInstruction[i-1]) * int(self.tmpInstruction[i-2]))
                        del self.tmpInstruction[i-2:i]
                        self.run(self.tmpInstruction)
                    elif self.tmpInstruction[i] == "/":
                        self.tmpInstruction[i] = str(int(self.tmpInstruction[i-1]) // int(self.tmpInstruction[i-2]))
                        del self.tmpInstruction[i-2:i]
                        self.run(self.tmpInstruction)
                    elif self.tmpInstruction[i] == "DUP":
                        self.tmpInstruction.insert(i-1,self.tmpInstruction[i-1])
                        del self.tmpInstruction[i+1]
                        self.run(self.tmpInstruction)
                    elif self.tmpInstruction[i] == "POP":
                        del self.tmpInstruction[i-1:i+1]
                        self.run(self.tmpInstruction)
                               
                           
            
    
    def getValue(self):
        self.do = False
        if self.tmpInstruction == 0:
            return 0
        for item in self.tmpInstruction:
            if item == "x":
                abort = "x"
                return('Invalid instruction: {}'.format(abort))
            else:
                if item == "y":
                    abort = "y"
                    return('Invalid instruction: {}'.format(abort))
        if self.tmpInstruction[-1].isdigit():
            return(int(self.tmpInstruction[-1]))
        else:
            return(self.tmpInstruction[-1])

