"""


Create a function that can take 1, 2, or 3 arguments (like the range function)
and returns a tuple. This should be able to return float values (as opposed to
the range function which can't take float values as a step).

### Examples

    drange(1.2, 5.9, 0.45) ➞ (1.2, 1.65, 2.1, 2.55, 3.0, 3.45, 3.9, 4.35, 4.8, 5.25, 5.7)
    
    drange(10) ➞ (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    
    drange(1, 7, 1.2) ➞ (1, 2.2, 3.4, 4.6, 5.8)
    # Here 7 is not included, like in the range function.

### Notes

Always round values to the number with the most decimal digits (e.g. in the
first example, the answer should always be rounded to 2 digits. In the second,
it should be rounded to 0 digits and the third, 1 digit).

"""

def drange(*args):
  f=[]
  w=[]
  if len(args)==1:
    for i in range(0,args[0]):
      f.append(i)
    return tuple(f)
  elif len(args)==2:
    for i in range(args[0],args[1]):
      f.append(i)
    return tuple(f)
  else:
    c=0
    s=0
    switch=False
    for d in args:
      d=str(d)
      for x in d:
        if switch==True:
          c+=1
        if x==".":
          switch=True
      if c>s:
        s=c
      c=0
      switch=False
    z=0
    while(True):
      if z==0:
        z=args[0]
      else:
        z=round(z+args[2],s)
      if z>=args[1]:
        w=tuple(w)
        return w
      else:
        w.append(z)

