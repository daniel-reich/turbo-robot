"""


Given a number, insert duplicate digits on both sides of all digits which
appear in a group of 1.

### Worked Example

    numbers_need_friends_too(22733) ➞ 2277733
    
    # The number can be split into groups 22, 7, and 33.
    # 7 appears on its own.
    # Put 7s on both sides to create 777.
    # Put the numbers together and return the result.

### Examples

    numbers_need_friends_too(123) ➞ 111222333
    
    numbers_need_friends_too(56657) ➞ 55566555777
    
    numbers_need_friends_too(33) ➞ 33

### Notes

All tests will include positive integers.

"""

def numbers_need_friends_too(n):
  
  Text = str(n)
  
  Blocks = []
  Batch = Text[0]
  
  Counter = 1
  Length = len(Text)
  
  while (Counter < Length):
    
    Item_A = Batch[-1]
    Item_B = Text[Counter]
    
    if (Item_A != Item_B) and (len(Batch) == 1):
      Batch = Batch + Item_A + Item_A
      Blocks.append(Batch)
      Batch = Item_B
      Counter += 1
    elif (Item_A != Item_B) and (len(Batch) > 1):
      Blocks.append(Batch)
      Batch = Item_B
      Counter += 1
    else:
      Batch = Batch + Item_B
      Counter += 1
  
  if (len(Batch) == 1):
    Batch = Batch + Batch[-1] + Batch[-1]
    Blocks.append(Batch)
  else:
    Blocks.append(Batch)
  
  Link = ""
  Merged = Link.join(Blocks)
  Answer = int(Merged)
  return Answer

