"""


Write a function that returns the greatest common divisor of all list
elements. If the greatest common divisor is `1`, return `1`.

### Examples

    GCD([10, 20, 40]) ➞ 10
    
    GCD([1, 2, 3, 100]) ➞ 1
    
    GCD([1024, 192, 2048, 512]) ➞ 64

### Notes

  * List elements are always greater than `0`.
  * There is a minimum of two list elements given.

"""

def GCD(lst):
  L = lcm_of_list(lst);
  return L;
  
  
def lcm_of_list(numbers):
  BIGL = [PF(i) for i in numbers]
  Mega = sorted(set(n for sublst in BIGL for n in sublst))
  uthere = [];
  listFinal = [];
  for i in Mega:
    Cnums = 0;    
    for miniL in BIGL:
      if i in miniL:
        
        uthere.append(1);
        
      else:
        uthere.append(0);   
    if all(uthere):
      Cnums = min(subL.count(i) for subL in BIGL)
      listFinal.append(i**Cnums);
    uthere = [];
  if len(listFinal)>0:
    multiN =1;
    for i in listFinal:
      multiN *= i
    return multiN;
  else:
    return 1;
​
  
def PF(X): #prime factors
    d = 2
    L = []
    while X != 1:
        #print(d, X,L)
        if X % d == 0:
            L.append(d)
            X = X // d
        else:
            d+=1
    return L

