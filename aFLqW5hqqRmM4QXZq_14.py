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
    result=results
    a,b,c,d=sorted([v for k, v in sorted(results.items())],reverse=True)
    f=sorted([k for k,v in results.items()])
    a=(int(a/50),a)
    b=(int(b/50),b)
    c=(int(c/50),c)
    d=(int(d/50),d)
    print([a,b,c,d])
    m=[a,b,c,d]
    z,e,p,l=[],[],'',[]
    for i in m:
        i=list(i)
        z.append('#'*i[0]+' '+str(i[1]))
        for k,v in sorted(results.items()):
            if i[1]==v and k not in e:
                 e.append(k)   
    for i in z:
        l.append(i.strip())
    x=[j+'|'+i for i,j in zip(l,e)]
    return '\n'.join(x)

