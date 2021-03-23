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
    result_n = []
​
    result_n_sum = 1
​
    [[result_n.append(b) for b in range(1, a+1) if a % b == 0 and b != 1]
     for a in range(1, n*4) if len([b for b in range(1, a+1) if a % b == 0 and b != 1]) == 1]
​
    result_n_final = result_n[0:n]
​
    i = 0
    for i in range(0, len(result_n_final)):
        result_n_sum = result_n_final[i] * result_n_sum
        i += 1
​
    return result_n_sum

