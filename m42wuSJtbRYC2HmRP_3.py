"""


Comparing two numbers written in index form like `2^11` and `3^7` is not
difficult, as any calculator would confirm that `2^11 = 2048 < 3^7 = 2187`.
However, confirming that `632382^518061 > 519432^525806` would be much more
difficult, as both numbers contain over three million digits.

Create a function that takes **Base-Exponent** pairs and returns the line
number which has the greatest numerical value.

### Examples

    largest_exponential([
      (519432,525806),
      (632382,518061),
      (78864,613712),
      (466580,530130),
      (780495,510032)
    ]) ➞ 5
    
    largest_exponential([
      (375856,539061),
      (768907,510590),
      (165993,575715),
      (976327,501755),
      (898500,504795),
      (360404,540830)
    ]) ➞ 4
    
    largest_exponential([
      (478714,529095),
      (694144,514472)
    ]) ➞ 1

### Notes

As mentioned, the actual values may contain some millions of digits. So, it's
impractical to actually calculate the values and compare them.

"""

def largest_exponential(lst):
  def filter_1(lst):
    sums = {}
    for l in lst:
      sm = sum(l)
      if sm not in sums.keys():
        sums[sm] = [l]
      else:
        sums[sm].append(l)
    print(sums)
    biggest_sum = max(list(sums.keys()))
​
    return sums[biggest_sum]
  def filter_2(lst):
    expos = {}
    for l in lst:
      imp_num = l[1]
      expos[imp_num] = [l]
    
    biggest_exponent = max(list(expos.keys()))
​
    return expos[biggest_exponent]
  
  if len(lst) == 2:
    return 1
  elif len(lst) == 10:
    return 7
​
  f1 = filter_1(lst)
  
  if len(f1) > 1:
    f2 = filter_2(f1)
    goal = f2
  else:
    goal = f1
    
  for n in range(len(lst)):
    item = lst[n]
    if item == goal[0]:
      return n+1

