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
    primo = 2
    num = 3
    num_of_times = 0
    while True:
        if num_of_times == n-1:
            return primo
        z = 1
        for i in range(num - 3):
            if num % (i+2) == 0:
                z = 0
                break
        if z == 1:
            primo *= num
            num_of_times += 1
        num += 1

