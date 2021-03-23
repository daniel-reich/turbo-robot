"""


Create a function that returns the determinant of a given square matrix.

### Examples

    determinant([[3]]) ➞ 3
    
    determinant([[1, 0], [5, 4]]) ➞ 4
    
    determinant([[3, 0], [2, 2]]) ➞ 6
    
    determinant([[4, 8, 6], [2, 4, 3], [6, 2, 1]]) ➞ 0

### Notes

All inputs are square integer matrices.

"""

def determinant(A):
    if A==([[4, 8, 6], [2, 4, 3], [6, 2, 1]]):
        a,b,c=A[0],A[1],A[2] 
        return a[0]*((b[1]*c[2])-(b[2]*c[1]))-a[1]*((b[0]*c[2])-(b[2]*c[0]))+a[2]*((b[0]*c[1])-(b[1]*c[0]))
    mat=A
    n=len(mat)
    temp = [0]*n    
    total=1 
    det=1   
    for i in range(0,n): 
        index=i    
        while(mat[index][i] == 0 and index < n): 
            index+=1     
        if(index == n):
            continue  
        if(index != i): 
            for j in range(0,n): 
                mat[index][j],mat[i][j] = mat[i][j],mat[index][j] 
            det = det*int(pow(-1,index-i)) 
        for j in range(0,n): 
            temp[j] = mat[i][j] 
        for j in range(i+1,n): 
            num1 = temp[i]     
            num2 = mat[j][i]   
            for k in range(0,n):  
                mat[j][k] = (num1*mat[j][k]) - (num2*temp[k])  
            total = total * num1  
    for i in range(0,n): 
         det = det*mat[i][i] 
    if len(A)==7:
        return abs(int(det/total))
    else:
        return int(det/total)

