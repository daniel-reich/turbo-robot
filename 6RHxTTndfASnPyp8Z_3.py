"""


The function is given an array of characters. Compress the array into a string
using the following rules. For each group of consecutively repeating
characters:

  * If the number of repeating characters is one, append the string with only this character.
  * If the number `n` of repeating characters `x` is greater than one, append the string with `"x" + str(n)`.

### Examples

    compress(["a", "a", "b", "b", "c", "c", "c"]) ➞ "a2b2c3"
    
    compress(["a"]) ➞ "a"
    
    compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) ➞ "ab12"
    
    compress(["a", "a", "a", "b", "b", "a", "a"]) ➞ "a3b2a2"

### Notes

N/A

"""

def compress(lst):
  res = "" 
​
  temp_lst = [] 
  counter = 0 
​
​
  for i in range(len(lst)):
​
    if not temp_lst:
      temp_lst.append(lst[0]) 
      counter += 1 
​
    else:
      next_ele = lst[i] 
​
      if temp_lst[-1] == next_ele:
        counter += 1 
​
      if temp_lst[-1] != next_ele:
        if counter == 1:
          pass
        else:
          temp_lst.append(str(counter)) 
​
        counter = 1
        temp_lst.append(lst[i]) 
​
      if i == len(lst) - 1:
        temp_lst.append(str(counter)) 
​
  return ("".join(temp_lst))

