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
    key = []
    value = []
    isi = ""
    for i in results.items():
        key += [i[0]]
        value += [i[1]]
  
    for i in range(len(key)):
        for j in range(len(key)-i-1):
            if value[j] > value[j+1]:
                value[j], value[j+1] = value[j+1], value[j]
                key[j], key[j+1] = key[j+1], key[j]
            elif value[j] == value[j+1] and int(key[j][1]) < int(key[j+1][1]):
                value[j], value[j+1] = value[j+1], value[j]
                key[j], key[j+1] = key[j+1], key[j]
​
    for i in range(len(key)-1, -1, -1):
        isi += key[i]+"|"
        banyak_pagar = int(value[i]/50)
        for j in range(banyak_pagar):
            isi += "#"
            if j == banyak_pagar-1:
                isi += " "
        isi += str(value[i])
        if i != 0:
            isi += "\n"
​
    return isi

