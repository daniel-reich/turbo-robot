"""
Given a **unordered** list of the vertices of a **convex** polygon, find its
area.

### Examples

    polygon([[2, 5], [5, 1], [-4, 3]]) ➞ 15.0
    
    polygon([[-1, 1], [1, 1], [-1, -1], [1, -1]]) ➞ 4.0
    
    polygon([[2, 2], [11, 2], [4, 10], [9, 7]]) ➞ 45.5
    
    polygon([[5, 3], [3, 4], [12, 8], [5, 11], [9, 5]]) ➞ 39.0

### Notes

  * A convex polygon has all interior angles less than 180 degrees.
  * The first example has only 3 vertices so this list is ordered by default.

"""

def polygon(A):
  import math
  [k,l]=[0,0]
  
  for i in A:
    k+=i[0]      #This for loop calculate the center of polygon
    l+=i[1]
​
  B=[k/len(A),l/len(A)] #This is the center of polygon
  
  vectors=[[math.atan2(A[i][0]-B[0],A[i][1]-B[1]), A[i]] for i in range(len(A))]  #This calculate arctan degree between center of array and every vector
  last_list=sorted(vectors, key= lambda x : x[0])   #This is sort the array based on arctan values
  last_list1=[i[1] for i in last_list] 
  last_list1.append(last_list1[0])   #This is add first element of list to the end of array
​
  area= lambda K,M: (K[1]*M[0]-K[0]*M[1])/2   
  summ=0
  for i in range(len(last_list1)-1):
    summ+=area(last_list1[i],last_list1[i+1])     #this calculates area based on area formula of polygon 
  return summ

