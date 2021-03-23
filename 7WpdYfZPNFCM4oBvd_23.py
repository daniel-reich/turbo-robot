"""
Make a function that takes a 2D list and returns `True` if it is a Magic
Square and `False` if it is not. A Magic Square is an arrangement of numbers
in a square in such a way that the sum of each row, column, and diagonal is
one constant number, the "magic constant".

### Examples

    is_magic([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) ➞ True
    
    # Rows: 2+7+6 = 9+5+1 = 4+3+8 = 15
    # Columns: 2+9+4 = 7+5+3 = 6+1+8 = 15
    # Diagonals: 2+5+8 = 6+5+4 = 15
    is_magic([[1, 2], [3, 4]]) ➞ False
    
    # Rows: 1+2 = 3 != 3+4 = 7
    # Columns: 1+3 = 4 != 2+4 = 6
    # Diagonals: 1+4 = 2+3 = 5

### Notes

For this challenge, I will only be testing with magic squares made with whole
numbers ranging from 1 to n^2.

"""

def is_magic(square):
        a=len(square)
        i,j,c,d,e,t,t1,t2=0,0,0,0,0,[],[],[]
        if a==0:
                return True
        elif a==1 and (square[0]!=[1]):
                return False
        else:
                b=sum(square[0])
        if b>(a+a**3)/2:
                return False
        while i<a:
                if len(square[i])!=a or sum(square[i])!=b:
                        return False
                else:
                        i+=1
        while j<a:
                while c<a:
                        t.append(square[c][j])
                        c+=1
                if sum(t)!=b:
                        return False
                else:
                        j+=1
        while d<a:
                while e<a:
                        t1.append(square[d][e])
                        t2.append(square[d][a-e-1])
                        d+=1
                        e+=1
        if sum(t1)!=b or sum(t2)!=b:
                return False
        return True

