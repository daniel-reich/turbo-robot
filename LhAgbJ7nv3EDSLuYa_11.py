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
    g = [0] * (n + 1)  
    g[1] = 1 
    for i in range(2, n + 1):  
        g[i] = 1 + g[i - g[g[i - 1]]]  
    return g[1:]
