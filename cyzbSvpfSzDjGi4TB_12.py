"""


In mathematics, the harmonic series is the divergent infinite series:

![Alternative Text](https://edabit-
challenges.s3.amazonaws.com/a741e7af8c9e50f3ad47c3ef7d9b903de7824608.svg)

Its name derives from the concept of overtones, or harmonics in music.

Create a function that, given a precision parameter, returns the value of the
harmonic series.

### Examples

    harmonic(3) ➞ 1.833
    
    harmonic(1) ➞ 1.0
    
    harmonic(5) ➞ 2.283

### Notes

Round the result to the third decimal place.

"""

def harmonic(n):
  s = 0
  for i in range(1,n+1):
    s += 1/i
  return round(s,3)

