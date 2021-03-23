"""


Python offers some bit operations but not bit rotation. To complete that,
create a function that takes three parameters:

  1. `n`: Integer, which in binary representaion should be rotated.
  2. `m`: Number of rotation steps that should be performed.
  3. `d`: Boolean value; `True` = rotation right, `False` = rotation left.

Your function should return an integer as a result of its rotated binary
representation.

### Examples

    bit_rotate(8, 1, True) ➞ 4
    # 8 in bin: 1000, rotated 1 step to the right: 0100, in dec: 4
    
    bit_rotate(16, 1, False) ➞ 1
    # 16 in bin: 10000, rotated 1 step to the left: 00001, in dec: 1
    
    bit_rotate(17, 2, False) ➞ 6
    # 17 in bin: 10001, rotated 2 steps to the left: 00110, in dec: 6

### Notes

  * For parameters use unsigned integers only.
  * There is a solution with string operations and combined bit operations.

"""

def bit_rotate(n,m,d):
  bin_num = bin(n)[2:]
  liste,indexes,final_indexes,final_bit = [],[],[],[]
  compteur = 0
  [liste.append(_) for _ in bin_num]
  for _ in liste:
    if _ == "1":
      indexes.append(compteur)
    compteur+=1
​
  [final_indexes.append((int(i)+m)%len(bin_num)) if d == True else final_indexes.append((int(i)-m)%len(bin_num)) for i in indexes]
  [final_bit.append("1") if _ in final_indexes else final_bit.append("0") for _ in range(len(bin_num))]
​
  return(int("".join(final_bit),base=2))

