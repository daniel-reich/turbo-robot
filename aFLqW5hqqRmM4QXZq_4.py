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

def bar_chart(sales):
  sales_reverse = {sales[i]:i for i in sales}
  sales_value_list = []
  
  for e in sales:
    if len(sales_value_list) == 0:
      sales_value_list.append(e)
    else:
      insert = False
      for i in range(len(sales_value_list)):
        if sales[e] > sales[sales_value_list[i]] or (sales[e] == sales[sales_value_list[i]] and e < sales_value_list[i]):
          sales_value_list.insert(i,e)
          insert = True
          break
      if insert == False:
        sales_value_list.append(e)
          
  result = ""
  for i,e in enumerate(sales_value_list):
    count = sales[e]//50
    if count == 0:
      result += (e + "|" + "0")
    else:
      result += (e + "|" + "#"*count + " "+ str(sales[e]))
    if i != 3:
      result += "\n"
  
  return result

