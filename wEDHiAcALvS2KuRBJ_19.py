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
        self.arg_list = None
        self.operators = []
        self.result = None
        self.instructions_list = {'+': self.plus_op,
                                  '-': self.minus_op,
                                  '*': self.mux_op,
                                  '/': self.div_op,
                                  'DUP': self.dup_op,
                                  'POP': self.pop_op
                                  }
​
    # @property
    # def parse(self,value):
    def plus_op(self):
        if len(self.stack) > 1:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a + b)
​
    def minus_op(self):
        if len(self.stack) > 1:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a - b) if a > b else self.stack.append(b - a)
​
    def mux_op(self):
        if len(self.stack) > 1:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a * b)
​
    def div_op(self):
        if len(self.stack) > 1:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a / b) if a > b else self.stack.append(b / a)
​
    def dup_op(self):
        if len(self.stack) > 0:
            self.stack.append(self.stack[-1])
​
    def pop_op(self):
        if len(self.stack) > 0:
            self.stack.pop()
​
    def run(self, instructions):
        self.arg_list = instructions.split()
        for i in range(len(self.arg_list)):
            if self.arg_list[i] not in self.instructions_list and self.arg_list[i].isnumeric():
                self.stack.append(int(self.arg_list[i]))
            elif self.arg_list[i] in self.instructions_list:
                self.instructions_list[self.arg_list[i]]()
            else:
                self.result = "Invalid instruction: {}".format(self.arg_list[i])
                return
        self.result = self.stack.pop() if self.stack else 0
​
    def getValue(self):
        return self.result
​
​
if __name__ == "__main__":
    tests = [
      {'arg': '12', 'ans': 12},
      {'arg': '5 6 +', 'ans': 11},
      {'arg': '3 6 -', 'ans': 3},
      {'arg': '3 DUP +', 'ans': 6},
      {'arg': '2 5 - 5 + DUP +', 'ans': 16},
      {'arg': '9 14 DUP + - 3 POP', 'ans': 19},
      {'arg': '1 2 3 4 5 POP POP POP', 'ans': 2},
      {'arg': '13 DUP 4 POP 5 DUP + DUP + -', 'ans': 7},
      {'arg': '6 5 5 7 * - /', 'ans': 5},
      {'arg': '4 2 4 * 3 + 5 + / 5 -', 'ans': 1},
      {'arg': '5 8 + 4 5 1 + POP 13 +', 'ans': 17},
      {'arg': 'x', 'ans': 'Invalid instruction: x'},
      {'arg': '4 6 + x', 'ans': 'Invalid instruction: x'},
      {'arg': 'y x *', 'ans': 'Invalid instruction: y'},
      {'arg': '', 'ans': 0},
      {'arg': '4 POP', 'ans': 0}
    ]
​
    for dict in tests:
        arg = dict['arg']
        ans = dict['ans']
        machine = StackCalc()
        machine.run(arg)
        assert machine.getValue() == ans

