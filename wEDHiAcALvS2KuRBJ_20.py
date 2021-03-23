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
        self.instructions = []
​
    def run(self, instructions):
        self.instructions = instructions.split()
​
    def getValue(self):
        two_number_operations = ['+', '-', "*", "/"]
        answer, stack = 0, []
        for i in self.instructions:
            if i.isdecimal():
                stack.append(int(i))
            elif i in two_number_operations:
                stack.append(
                    eval(
                        str(max(stack[-2:])) 
                        + i 
                        + str(min(stack[-2:]))
                    )
                )
                stack.pop(-3)
                stack.pop(-2)    
            elif i == "DUP":
                stack.append(stack[-1])
            elif i == "POP":
                stack.pop(-1)    
            else:
                return "Invalid instruction: " + i
        if len(stack) >= 1:
            answer = stack[-1]
        return answer

