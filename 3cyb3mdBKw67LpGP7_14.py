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

def numbers_need_friends_too(m):
  qq=str(m)
  n=[int(i) for i in qq]
  index=[]
  for i in range(0,len(n)-1):
    if n[i] != n[i+1]:
      index.append(i)     
  index= [x+1 for x in index]
  final_lst=[]
  for i,j in zip([0]+index,index+[None]):
    if len(n[i:j])<2:
      temp_lst=n[i:j]+n[i:j]+n[i:j]
    else:
      temp_lst=n[i:j]
    final_lst.extend(temp_lst)
  qqq=[str(i) for i in final_lst]
  a_a="".join(qqq)
  return int(a_a)

