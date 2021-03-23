"""


 **Mubashir** needs your help to find out **number of animals** hidden in a
given string `txt`.

You are provided with an array of animals given below:

    animals = ["dog", "cat", "bat", "cock", "cow", "pig",
    "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
    "frog", "hen", "mole", "duck", "goat"]

 **Rule:** Return the **maximum number** of animal names. See the below
example:

    txt = "goatcode"
    
    count_animals(txt) ➞ 2
    # First animal = "dog"
    # Remaining string = "atcoe",
    # Second animal = "cat".
    # count = 2 (correct)
    
    # If you got a "goat" first time
    # remaining string = "code",
    # no animal will be found during next time.
    # count = 1 (wrong)

### Examples

    count_animals("goatcode") ➞ 2
    # "dog", "cat"
    
    count_animals("cockdogwdufrbir") ➞ 4
    # "cow", "duck", "frog", "bird"
    
    count_animals("dogdogdogdogdog") ➞ 5

### Notes

N/A

"""

import math
animals = ["dog", "cat", "bat", "cock", "cow", "pig", 
  "fox", "ant", "bird", "lion", "wolf", "deer", "bear", 
  "frog", "hen", "mole", "duck", "goat"]
​
def chars(txt):
  tmp=[0]*256
  for i in txt:
    tmp[ord(i)] += 1
  return tmp
​
​
​
def count_animals2(txt):
  data=chars(txt)
  counting=0
  print(txt)
​
  for a in animals:
    tmp=chars(a)
    max=99999
    for d,t in zip(data,tmp):
      if t>0:
        max=min(max,math.floor(d/t))
    if max>0:
      print(max,a)
    counting += max
    for count,t in enumerate(tmp):
      data[count] -= t*max
  for i,a in enumerate(data):
    if a>0:
      print(a,chr(i))
  
  return counting
  
def count_animals(txt):
  tmp=count_animals2(txt)
  animals.reverse()
  tmp=max(tmp,count_animals2(txt) )
  return tmp

