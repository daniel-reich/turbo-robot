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
  lst = []
  for i in ["Q1", "Q2", "Q3", "Q4"]:
    lst.append(Quarter(i, results[i]))
  lst.sort()
  lst.reverse()
  ret = []
  for i in lst:
    if i.result == 0:
      ret.append(i.name+"|"+"#"*(i.result//50)+str(i.result))
    else:
      ret.append(i.name+"|"+"#"*(i.result//50)+" "+str(i.result))
  return "\n".join(ret)
  
  
    
​
class Quarter(object):
  def __init__(self, name, result):
    self.name = name
    self.result = result
    
  def __lt__(self, other):
    return (self.result, other.name) < (other.result, self.name)
    
  def __repr__(self):
    if self.result == 0:
      return self.name+"|"+"#"*(self.result//50)+str(self.result)
    else:
      return self.name+"|"+"#"*(self.result//50)+" "+str(self.result)

