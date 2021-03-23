"""


 **Mubashir** needs your help to learn Python Programming. Help him by
modifying a given string `txt` as follows:

  * Reverse the string given.
  * Replace each letter to its position in the alphabet for example (a = 1, b = 2, c = 3, ...).
  * Join the array and convert it to a number.
  * Convert the number to binary.
  * Convert the string back to a number.

See below example for more understanding :

 **modify("hello") ➞ 111001101011101101101010**

     "hello" = "olleh"
     
     "olleh" = ['15', '12', '12', '5', '8']
     
     ['15', '12', '12', '5', '8'] = 15121258
     
     15121258 = "111001101011101101101010"
     
     "111001101011101101101010" = 111001101011101101101010

### Examples

    modify("hello") ➞ 111001101011101101101010
    
    modify("mubashir") ➞ 10110000110010000110011111000111000001
    
    modify("edabit") ➞ 111111110110001110001

### Notes

There are no spaces and the string is lowercase.

"""

class Base:
​
  def __init__(self, base):
    self.b = base
  
  def convert_from_int(self, inte):
​
    nums = [1]
    expo = 1
​
    while max(nums) < inte:
      nums.append(self.b**expo)
      expo += 1
    
    nums = list(reversed(nums))
​
    new_num = []
​
    for num in nums:
      if num <= inte:
        new_num.append(inte // num)
        inte = inte % num
      else:
        new_num.append(0)
    
    return int(''.join([str(i) for i in new_num]))
​
b2 = Base(2)
​
​
def modify(txt):
  
  txt = ''.join(list(reversed(txt))).lower()
​
  a = 'abcdefghijklmnopqrstuvwxyz'
  
  txt_nums = int(''.join([str(a.index(l8r) + 1) for l8r in txt]))
  
  return b2.convert_from_int(txt_nums)

