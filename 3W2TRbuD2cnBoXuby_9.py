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
  return sorted([s[i:i+n] for i in range(0,len(s)-n+1,n)])

