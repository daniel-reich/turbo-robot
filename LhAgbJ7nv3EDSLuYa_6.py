"""


The Golomb sequence is uniquely defined by the following rules:

  1. All terms are positive integers.
  2. No term is smaller than any previous term.
  3. The nth term is equal to the total number of times that the integer n appears within the sequence.

Write a function that returns the first n terms of the Golomb sequence as a
list.

### Examples

    golomb(1) ➞ [1]
    
    golomb(8) ➞ [1, 2, 2, 3, 3, 4, 4, 4]
    
    golomb(10) ➞ [1, 2, 2, 3, 3, 4, 4, 4, 5, 5]

1 appears once; 2 appears twice; 3 appears twice; 4 appears 3 times; 5 will
appear 3 times in the full sequence, etc.

### Notes

  * The tests will consist of random inputs between 1 and 1000 inclusive.
  * If stuck, see resources tab for more information and hints.

"""

def golomb(n):
    if n==1:
        return [1]
    s=[0]*(n+1)
    s[1]=1
    s[2]=2
    k=1
    i=2
    j=2
    while j<n+1:
        if j-k==s[i]:
            s[j]=i
            k=j
            j+=1
            i+=1
        else :
            s[j]=i
            j+=1
    return s[1:]

