"""


Replace the numbers in a string with their binary form.

### Examples

    replace_nums("I have 2 sheep.") ➞ "I have 10 sheep."
    
    replace_nums("My father was born in 1974.10.25.") ➞ "My father was born in 11110110110.1010.11001."
    
    replace_nums("10hell76o4 boi") ➞ "1010hell1001100o100 boi"

### Notes

  * There are possibly two or more numbers in a single word (I do not recommend splitting the text at spaces, it surely won't help).
  * Anything separates two numbers, even spaces ("2 2" --> "10 10").

"""

def replace_nums(string):
  n = ''.join([i if i.isdigit() else ' ' for i in string]).split()
  n = [d_to_b(int(i)) for i in n]
  ret = ''
  for i in range(len(string)):
    if not string[i].isdigit():
      ret+=string[i]
    elif string[i].isdigit():
      if i==0 or (i>0 and not string[i-1].isdigit()):
        ret+=n[0]
        n = n[1:]
  return ret
  
def d_to_b(n):
  ret = ''
  while n>0:
    ret+=str(n%2)
    n//=2
  return ret[::-1] if ret else '0'

