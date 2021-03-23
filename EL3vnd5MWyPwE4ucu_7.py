"""


Create a function to return the Nth number in the Fibonacci sequence as a
string.

### Examples

    fibonacci(10) ➞ "55"
    
    fibonacci(20) ➞ "6765"
    
    fibonacci(30) ➞ "832040"
    
    fibonacci(40) ➞ "102334155"
    
    fibonacci(50) ➞ "12586269025"
    
    fibonacci(60) ➞ "1548008755920"

### Notes

Your function is expected to calculate numbers greater than the 64-bit
unsigned integer limit where `n` can be as large as but not greater than 200.

"""

class Fibonacci:
  
  def __init__(self):
    self.seq = [0, 1, 1]
  
  def advance_to(self, goal):
    while len(self.seq) <= goal:
      self.seq.append(self.seq[-2] + self.seq[-1])
    return True
  
  def number_yet_found(self, number):
    return number <= len(self.seq)
    
  def retrieve(self, index):
    return self.seq[index]
​
f = Fibonacci()
​
def fibonacci(n):
  if f.number_yet_found(n) == False:
    f.advance_to(n)
  return str(f.retrieve(n))

