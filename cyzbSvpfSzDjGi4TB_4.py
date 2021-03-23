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
  if(n == 0):
    return 0
  if(n == 1):
    return 1
  else:
    fact = 1
    #for i in range(1,(n+1)):
    # fact = fact*i
    f = 1 
    t = 1
    for i in range(2,(n+1)):
      t = i*t + f
      f = f*i
    r = float(0)
    r = float((t)/(f))
    r = round(r,3)
    return r

