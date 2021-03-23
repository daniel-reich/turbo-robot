"""


Write a function that returns a list of strings populated from the slices of
**n-length** characters of the given word (a slice after another while
**n-length** applies onto the word).

### Examples

    collect("intercontinentalisationalism", 6)
    ➞ ["ationa", "interc", "ntalis", "ontine"]
    
    collect("strengths", 3)
    ➞ ["eng", "str", "ths"]
    
    collect("pneumonoultramicroscopicsilicovolcanoconiosis", 15)
    ➞ ["croscopicsilico", "pneumonoultrami", "volcanoconiosis"]

### Notes

  * Ensure that the resulting array is lexicographically ordered.
  * Return an **empty** array if the _given string_ is less than `n`.
  * A recursive version of this challenge can be found via this [link](https://edabit.com/challenge/TcKZnbdgx7q6LLoFR).

"""

def collect(s, n):
    slices = []
    if len(s) < n:
        return []
    for i in range(len(s)):
        if i % n == 0:
            slices.append(s[i:i+n])
    slices = sorted(slices)
    new_slices = []
    for i in range(len(slices)):
        if len(slices[i]) == n:
            new_slices.append(slices[i])
​
    return new_slices

