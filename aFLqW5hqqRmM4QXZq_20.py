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
    l = list(results.keys())
    l.sort(key=lambda x:results[x])
    l.reverse()
    d = {}
    for k in l:
        if(d.get(results[k]) == None):
            d[results[k]] = []
        ll = d[results[k]]
        ll.append(k)
        ll.sort()
        d[results[k]] = ll
    
    #print(l)
    #print(d)
    la = list(d.keys())
    la.sort()
    la.reverse()
    #print('LA',la)
    s = ''
    for k in la:
        for key in d[k]:
            #print(key, results[key])
            if(results[key] == 0):
                s = s + key + '|' + '0' + '\n'
            else:
                s = (s + key + '|' + '#'*int(results[key] / 50) +
                    ' ' + str(results[key]) + '\n')
    s = s.strip()
    return s

