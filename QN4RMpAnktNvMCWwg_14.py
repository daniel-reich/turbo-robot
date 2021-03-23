"""


An identity matrix is defined as a square matrix with **1s** running from the
top left of the square to the bottom right. The rest are **0s**. The identity
matrix has applications ranging from machine learning to the general theory of
relativity.

Create a function that takes an integer `n` and returns the identity matrix of
`n x n` dimensions. For this challenge, if the integer is negative, return the
mirror image of the identity matrix of `n x n` dimensions.. It does not matter
if the mirror image is left-right or top-bottom.

### Examples

    id_mtrx(2) ➞ [
      [1, 0],
      [0, 1]
    ]
    
    id_mtrx(-2) ➞ [
      [0, 1],
      [1, 0]
    ]
    
    id_mtrx(0) ➞ []

### Notes

Incompatible types passed as `n` should return the string `"Error"`.

"""

def id_mtrx(n):
    my_zero_mtrx = []
    if (type(n) == str):
        return "Error"
    my_list = [0]*n
    my_zero_list = []
    my_idt_mtrx = []
    
    if (n==0):
        my_idt_mtrx = [[]]
        return my_idt_mtrx
    
    elif (n>0):
        j=0
        for i in range (0,n):
            my_zero_mtrx.append(my_list)
        for i in range (0,len(my_zero_mtrx)):
            my_zero_list = my_zero_mtrx[i]
            my_zero_list = [0]*n
            my_zero_list[j] = 1
            my_idt_mtrx.append(my_zero_list)
            j+=1
        return my_idt_mtrx
    elif (n<0):
        j = len(my_list)-1
        for i in range (0,abs(n)):
            my_zero_mtrx.append(my_list)
        for i in range (0,len(my_zero_mtrx)):
            my_zero_list = my_zero_mtrx[i]
            my_zero_list = [0]*abs(n)
            my_zero_list[j] = 1
            my_idt_mtrx.append(my_zero_list)
            j-=1
        return my_idt_mtrx
        
        
 
​
print(id_mtrx("4"))

