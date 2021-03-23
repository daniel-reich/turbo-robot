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
  chart = ""
  q1 = "Q1|" + "#" * (results["Q1"]//50) +" {}\n".format(results["Q1"])
  q2 = "Q2|" + "#" * (results["Q2"]//50) +" {}\n".format(results["Q2"])
  q3 = "Q3|" + "#" * (results["Q3"]//50) +" {}\n".format(results["Q3"])
  q4 = "Q4|" + "#" * (results["Q4"]//50) +" {}\n".format(results["Q4"])
  
  qorder = [q[0] for q in sorted(list(results.items()), key=lambda x:(-x[1], x[0]))]
  for q in qorder:
    if q == 'Q1':
      chart += q1
    elif q == 'Q2':
      chart += q2
    elif q == 'Q3':
      chart += q3
    elif q == 'Q4':
      chart += q4
  return chart.replace(' 0','0')[:-1]

