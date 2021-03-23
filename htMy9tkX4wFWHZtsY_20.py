"""


Create a function that counts number of palindromes within two timestamps
inclusive. A palindrome is a timestamp that can be read the same from left to
right and from right to left (e.g. `02:11:20`).

### Examples

    palindrome_time([2, 12, 22, 4, 35, 10]) ➞ 14
    
    palindrome_time([12, 12, 12, 13, 13, 13]) ➞ 6
    
    palindrome_time([6, 33, 15, 9, 55, 10]) ➞ 0

### Notes

Input list contains six numbers `[h1, m1, s1, h2, m2, s2]` for begin and end
timestamps.

"""

def palindrome_time(lst):
​
  class Timestamp:
​
    def __init__(self, hour, minn, sec):
      self.h = str(hour)
      self.m = str(minn)
      self.s = str(sec)
​
      self.max_sec = sec + (minn * 60) + (hour * 60 * 60)
​
      if len(self.h) == 1:
        self.h = '0' + self.h
      if len(self.m) == 1:
        self.m = '0' + self.m
      if len(self.s) == 1:
        self.s = '0' + self.s
​
      self.rh = ''.join(list(reversed(self.h)))
      self.rm = ''.join(list(reversed(self.m)))
      self.rs = ''.join(list(reversed(self.s)))
​
      self.is_palindrome = ':'.join([self.h, self.m, self.s]) == ':'.join([self.rs, self.rm, self.rh])
​
    def find_time_in_range(self, other):
​
      start_time = self.max_sec
      end_time = other.max_sec
​
      palindromes = [self, other]
​
      for second in range(start_time + 1, end_time):
​
        ch,rs = int(second/(60*60)), int(second%(60*60))
        cm,cs = int(rs/60), int(rs%60)
​
        palindromes.append(Timestamp(ch,cm,cs))
      
      return palindromes
​
  t1 = Timestamp(lst[0], lst[1], lst[2])
  t2 = Timestamp(lst[3], lst[4], lst[5])
​
  if t1.h == t2.h and t1.m == t2.m and t1.s == t2.s:
    return 1
    
  timestamps = t1.find_time_in_range(t2)
  palindromes = 0
​
  for timestamp in timestamps:
    if timestamp.is_palindrome == True:
      palindromes += 1
  
  return palindromes

