"""


The Farey sequence of order `n` is the set of all fractions with a denominator
between 1 and `n`, reduced and returned in ascending order. Given `n`, return
the Farey sequence as a list, with each fraction being represented by a string
in the form "numerator/denominator".

### Examples

    farey(1) ➞ ["0/1", "1/1"]
    
    farey(4) ➞ ["0/1", "1/4", "1/3", "1/2", "2/3", "3/4", "1/1"]
    
    farey(5) ➞ ["0/1", "1/5", "1/4", "1/3", "2/5", "1/2", "3/5", "2/3", "3/4", "4/5", "1/1"]

### Notes

The Farey sequence will always begin with "0/1" and end with "1/1".

"""

def farey(n):
    numbers = []
    results = []
    org_results = []
    sol = []
    real_sol = []
    for x in range(n+1):
        numbers.append(x)
​
​
​
    for x in range(len(numbers)):
        for y in numbers:
            if y != 0:
                z = numbers[x] / y
                if z not in results and z < 1:
                    results.append(z)
                    sol.append(str(numbers[x])+"/"+str(y))
​
    for x in results:
        org_results.append(x)
    results.sort()
​
    for x in results:
​
        real_sol.append(sol[org_results.index(x)])
    real_sol.append("1/1")
    print(real_sol)
    return real_sol

