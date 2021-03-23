"""


Given a dictionary containing quarterly sales values for a year, return a
string representing a _bar chart_ of the sales by quarter.

  * Quarter names (Q1, Q2, Q3, Q4) should appear on the left.
  * Quarters should be sorted in descending order by value.
  * Quarters with the same value should be shown in their yearly order (Q1 -> Q4).
  * Bars should begin with a "|".
  * Repeat the character "#" to fill the bar, with each character having a value of 50.
  * A single space comes after the bar, then the sales for that quarter.
  * If the value is 0, there should be no space after "|".
  * Use the newline character ("\n") to separate each bar in the chart.

### Example #1

    bar_chart({"Q4": 250, "Q1": 300, "Q2": 150, "Q3": 0})
    ➞ "Q1|###### 300\nQ4|##### 250\nQ2|### 150\nQ3|0"

When printed:

    Q1|###### 300
    Q4|##### 250
    Q2|### 150
    Q3|0

### Example #2

    bar_chart({"Q4": 500, "Q3": 100, "Q2": 100, "Q1": 150})
    ➞ "Q4|########## 500\nQ1|### 150\nQ2|## 100\nQ3|## 100"

When printed:

    Q4|########## 500
    Q1|### 150
    Q2|## 100
    Q3|## 100

### Notes

There should be no additional whitespace after each value.

"""

def bar_chart(results):
  a = sorted([[k, v] for v, k in results.items()], reverse=True)
  rv = list(results.values())
  idx, qs = [], []
  for i, q in enumerate(a):
    if rv.count(q[0]) > 1:
      idx += [i]
      qs += [q]
  if len(idx) > 0:
    qs = sorted(qs)
    for i, x in zip(idx,qs):
      a[i] = x
  r = ""
  for q in a:
    r += q[1] + "|" + "#" * int(q[0]/50)
    if q[0] == 0: r+= str(q[0])
    else: r += " " +str(q[0])
    r += "\n"
  return r[:-1]

