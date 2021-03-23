"""


You will be given a simple string expression representing an addition or
subtraction in 8-bit 2's complement arithmetic. Write a function that returns
the result in base 10 followed by a binary representation. If any of the
values are outside the range of 8-bit 2's complement, return `"Overflow"`.

### Examples

    eight_bit("3 + 12") ➞ (15, "11 + 1100 = 1111")
    
    eight_bit("3 - 12") ➞ (-9, "11 - 1100 = 11110111")
    
    eight_bit(-18 - 6) ➞ (-24, "11101110 - 110 = 11101000")
    
    eight_bit(65 + 70) ➞ "Overflow"
    
    eight_bit(-127 + 127) ➞ (0, "10000001 + 1111111 = 0")

### Notes

Numbers in 8-bit 2's complement notation can range from -128 to 127. The
eighth (leftmost) bit signifies a negative number. See **Resources** for
details.

"""

def eight_bit(exp):
​
  class Base:
​
    def __init__(self, base):
      self.b = base
    
    def convert(self, b10_num):
​
      divisors = [1]
​
      for n in range(1, 8):
        divisors.append(2**n)
      
      bin_nums = []
​
      for divisor in reversed(divisors):
        bin_nums.append(str(int(b10_num / divisor)))
        b10_num = b10_num % divisor
      
      return ''.join(bin_nums)
    
    def add_nums(self, n1, n2):
​
      return self.convert(int(n1, 2) + n2)
​
  def invert(string):
    inverted = ''
    for item in string:
      if int(item) == 0:
        inverted += '1'
      else:
        inverted += '0'
    return inverted
​
  b2 = Base(2)
​
  if ' + ' in exp:
    nums = [int(n) for n in exp.split(' + ')]
    expression = '+'
  elif ' - ' in exp:
    nums = [int(n) for n in exp.split(' - ')]
    expression = '-'
  
  numbers = {}
​
  for n in range(len(nums)):
    num = nums[n]
​
    if num >= 0:
      numbers[n] = b2.convert(num)
    else:
      converted = b2.convert(abs(num))
      inverted = invert(converted)
      numbers[n] = b2.add_nums(inverted, 1)
    
    print(num, numbers)
  
  answer = eval(exp)
  
  if answer not in range(-128, 128):
    return 'Overflow'
  for number in nums:
    if number not in range(-128, 128):
      return 'Overflow'
​
  if answer >= 0:
    numbers['a'] = b2.convert(answer)
  else:
    converted = b2.convert(abs(answer))
    inverted = invert(converted)
    numbers['a'] = b2.add_nums(inverted, 1)
  
  return answer, '{} {} {} = {}'.format(int(numbers[0]), expression, int(numbers[1]), int(numbers['a']))

