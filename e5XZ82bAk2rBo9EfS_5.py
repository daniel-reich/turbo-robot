"""


Given a series of lists, with each individual list containing the **time of
the alarm set** and the **sleep duration** , return **what time to sleep**.

### Examples

    bed_time(["07:50", "07:50"]) ➞ ["00:00"]
    # The second argument means 7 hours, 50 minutes sleep duration.
    
    bed_time(["06:15", "10:00"], ["08:00", "10:00"], ["09:30", "10:00"]) ➞ ["20:15", "22:00", "23:30"]
    # The second argument of each sub list means 10 hours sleep duration.
    
    bed_time(["05:45", "04:00"], ["07:10", "04:30"]) ➞ ["01:45", "02:40"]
    # Sleep duration can be different among the lists.

### Notes

  * Times should be given in 24-hrs (i.e. "23:25" as opposed to "11:25PM").
  * Return a list of strings.

"""

def bed_time(*times):
  v=""
  b=""
  a=""
  e=""
  f=""
  l=[]
  switch=False
  for t in times:
    for c in t[0]:
      if switch==True:
        b=b+c
      elif c==":":
        v=int(v)
        switch=True
      elif switch==False:
        v=v+c
    b=int(b)
    switch=False
    for c in t[1]:
      if switch==True:
        e=e+c
      elif c==":":
        a=int(a)
        switch=True
      elif switch==False:
        a=a+c
    e=int(e)
    switch=False
    z=v-a
    w=b-e
    if w<0:
      z=z-1
      w=b+e
      w=abs(w)
    if w<10:
      w="0"+str(w)
    else:
      w=str(w)
    if z<0:
      z=24+z
    if z<10:
      z="0"+str(z)
    else:
      z=str(z)
    f=z+":"+w
    l.append(f)
    v=""
    b=""
    a=""
    e=""
    f=""
  return l

