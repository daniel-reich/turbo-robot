"""


 **Nesting level** , in this challenge, refers to the depth of parentheses
around an integer. For example, in the string `"(5((10)8))"`, 5 has a nesting
level of 1 because it has one set of parentheses around it, 10 has a nesting
level of 3 because it has 3 sets of parentheses around it, and 8 has a nesting
level of 2.

We can score this string by multiplying each number times its nesting level
and then summing the results:

    "(5((10)8))" ➞ 5*1 + 10*3 + 8*2 ➞ 51

Create a function that takes a string as its argument and returns its score.

### Examples

    score_it("()") ➞ 0
    
    score_it("4(123)") ➞ 123
    # 4*0 + 123*1 = 123
    
    score_it("((((1)2)3)4)") ➞ 20
    # 1*4 + 2*3 + 3*2 + 4*1 = 20
    
    score_it("(6)8((34(7)))") ➞ 95
    # 6*1 + 8*0 + 34*2 + 7*3 = 95

### Notes

  * The nesting for all test cases is balanced and logically consistent (there are no missing or extra parentheses).
  * Test cases contain only positive integers.

"""

def score_it(s):
  def nest(string, index):
​
    nsts = 0
​
    for n in range(index + 1):
      item = string[n]
      if item == '(':
        nsts += 1
      if item == ')':
        nsts -= 1
    
    return nsts
  def integers(lst, string):
    together = []
    near = []
​
    for idx in lst:
      if near == []:
        near.append(idx)
      else:
        if idx == max(near) + 1:
          near.append(idx)
        else:
          together.append(near)
          near = [idx]
    
    if near != []:
      together.append(near)
    del near
    
    numbers = []
    
    for lst in together:
      nums = []
      for idx in lst:
        try:
          nums.append(str(int(string[idx])))
        except ValueError:
          pass
      if len(nums) != 0:
​
        num = ''.join(nums)
        numbers.append(int(num))
    
    if len(numbers) == 0:
      return [0]
    return numbers
​
  nests = {}
​
  for n in range(len(s)):
    nst = nest(s, n)
    if nst not in nests.keys():
      nests[nst] = [n]
    else:
      nests[nst].append(n)
  
  nest_vals = {}
​
  for ky in nests.keys():
    nest_vals[ky] = integers(nests[ky], s)
  
  score = 0
​
  for val in nest_vals.keys():
    integers = nest_vals[val]
​
    for integer in integers:
      score += (integer * val)
    
  return score

