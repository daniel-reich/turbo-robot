"""


A _Primorial_ is a product of the first `n` prime numbers (e.g. `2 x 3 x 5 =
30`). `2, 3, 5, 7, 11, 13` are prime numbers. If `n` was `3`, you'd multiply
`2 x 3 x 5 = 30` or Primorial = `30`.

Create a function that returns the Primorial of a number.

### Examples

    primorial(1) ➞ 2
    
    primorial(2) ➞ 6
    
    primorial(8) ➞ 9699690

### Notes

N/A

"""

def primorial(n):
    list1 = []
    for i in range(2,100):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            list1.append(i)
    sum1 = 1
    for k in list1[0:n]:
        sum1 *= k
    return sum1

