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
​
    def prime(num):
        for i in range(2,int(num/2)+1):
            if num%i == 0:
                return False
        return True
​
​
    output = 1
    i = 2
    count = 0
    while count<n:
        if prime(i):
            output = output * i
            count += 1
            print(i, prime(i))
        i+=1
    return output

