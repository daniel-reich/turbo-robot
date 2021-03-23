"""


Given an amount of **money** and a list of **coins denominations** , create a
function that counts how many different ways you can make change with the
given money.

### Examples

    coins_combinations(4, [1, 2]) ➞ 3
    # 1+1+1+1 = 4
    # 1+1+2 = 4
    # 2+2 = 4
    
    coins_combinations(10, [5, 2, 3]) ➞ 4
    
    coins_combinations(11, [5, 7]) ➞ 0

### Notes

  * Order of coins does not matter (i.e. 1+1+2 == 2+1+1).
  * You have an infinite amount of coins.

"""

def coins_combinations(m, c):
  size=len(c)
  c.sort()
  sm=[[0]*(m+1) for n in range(size)]   
  for j in range(size):            
    for k in range(m+1):  
      if j==0:sm[0][k]=(k%c[0]==0)*1
      elif k<c[j]:sm[j][k]=sm[j-1][k]
      elif k==c[j]:sm[j][k]=sm[j][0]+sm[j-1][k]
      else: sm[j][k]=sm[j][k-c[j]]+sm[j-1][k]
  return sm[-1][-1]

