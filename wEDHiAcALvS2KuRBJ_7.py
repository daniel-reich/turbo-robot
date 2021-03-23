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
    self.value=0
  
  def run(self, instructions):
    self.instructions = instructions
    self.lst = [x for x in self.instructions.split()]
    self.curr =[]
    if (len(self.lst)==0):
      self.value =0
      return self.value
    else:
      for i in range (len(self.lst)):
        if (len (self.curr)==0):
          if self.lst[i].isnumeric():
            self.curr.append(self.lst[i])
          else:
            self.value='Invalid instruction: ' + str (self.lst[i])
            return self.value
        else:
          if self.lst[i].isnumeric():
            self.curr.append(self.lst[i])
          elif self.lst[i]== 'DUP':
            self.curr.append(self.curr[-1])
          elif self.lst[i]== 'POP':
            self.curr.pop(-1)
          elif self.lst[i] in ['+','-','*','/']:
            
            if self.lst[i] == '+':
              self.curr[-1]=int(self.curr[-1])+int(self.curr[-2])
              self.curr.pop(-2)
            elif self.lst[i] == '-':
              self.curr[-1]=int(self.curr[-1])-int(self.curr[-2])
              self.curr.pop(-2)
            elif self.lst[i] == '*':
              self.curr[-1]=int(self.curr[-1])*int(self.curr[-2])
              self.curr.pop(-2)
            else:
              self.curr[-1]=int(self.curr[-1])/int(self.curr[-2])
              self.curr.pop(-2)
            
          else:
            self.value = 'Invalid instruction: ' + str (self.lst[i])
            return self.value
      self.value = int(self.curr[-1]) if len(self.curr)>0  else 0
      return self.value
​
  def getValue(self):
    return self.value

