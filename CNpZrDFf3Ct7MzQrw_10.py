"""


Create a function that takes two integers and returns `true` if a digit
repeats three times in a row at any place in `num1` **AND** that same digit
repeats two times in a row in `num2`.

### Examples

    trouble(451999277, 41177722899) ➞ True
    
    trouble(1222345, 12345) ➞ False
    
    trouble(666789, 12345667) ➞ True
    
    trouble(33789, 12345337) ➞ False

### Notes

You can expect every test case to contain exactly two integers.

"""

def trouble(num1, num2):
  string1 = False
  string2 = False
  rep_num = 0
  count = 1
  for n in range(len(str(num1)) - 1):
    if str(num1)[n] == str(num1)[n+1]:
      count += 1
      print(count)
      if count == 3:
        rep_num = int(str(num1)[n])
        string1 = True
        count = 1
        break
  if str(num2).count(str(rep_num)) >= 2:
    string2 = True
  print(str(string1) + ", " + str(string2))
  if string1 and string2:
    return True
  else:
    return False

