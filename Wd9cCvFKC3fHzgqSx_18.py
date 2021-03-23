"""


Create a function that takes a number `num` and returns each place value in
the number.

### Examples

    num_split(39) ➞ [30, 9]
    
    num_split(-434) ➞ [-400, -30, -4]
    
    num_split(100) ➞ [100, 0, 0]

### Notes

N/A

"""

def num_split(num):
  
  class Number:
    def get_ten_thousands(num):
      return 10000 * (num // 10000)
    def get_thousands(num):
      return 1000 * (num // 1000)
    def get_hundreds(num):
      return 100 * (num // 100)
    def get_tens(num):
      return 10 * (num // 10)
    
    def __init__(self, number):
      self.n = number
      self.an = abs(number)
      
      self.tth = None
      self.th = None
      self.h = None
      self.t = None
      self.o = None
      
      if self.an >= 10000:
        self.tth = Number.get_ten_thousands(int(str(self.an)[-5:]))
      if self.an >= 1000:
        self.th = Number.get_thousands(int(str(self.an)[-4:]))
      if self.an >= 100:
        self.h = Number.get_hundreds(int(str(self.an)[-3:]))
      if self.an >= 10:
        self.t = Number.get_tens(int(str(self.an)[-2:]))
      if self.an >= 1:
        self.o = int(str(self.an)[-1])
      
      if self.n < 0:
        try:
          self.tth *= -1
        except TypeError:
          pass
        try:
          self.th *= -1
        except TypeError:
          pass
        try:
          self.h *= -1
        except TypeError:
          pass
        try:
          self.t *= -1
        except TypeError:
          pass
        try:
          self.o *= -1
        except TypeError:
          pass
          
    def display(self):
      tr = []
      for item in [self.tth, self.th, self.h, self.t, self.o]:
        if item != None:
          tr.append(item)
      return tr
  
  n = Number(num)
  
  return n.display()

