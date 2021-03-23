"""


The Edabit Medical Industries are developing a new drug, the _Edabitin™_ ,
which will (hopefully) increase the programming skills of patients. Various
tests are carried out on different programmers: for a week some are given the
_Edabitin™_ , while others are supplied simple _generic Tutorial powder_.
After a week, the number of programmers able to solve ten exercises of an
average level in half an hour and the number of those that instead take two
hours is recorded for both control groups.

You are asked to establish if _Edabitin™_ has a statistical influence over
performances with a **Chi-Squared Test**.

Look at the table below:

Treatment| 2 Hours| ½ Hour  
---|---|---  
Edabitin| 207| 282  
Tutorial| 231| 242  
  
The first thing to do is to calculate the total population of programmers
involved in the test, so you have to sum all the four cells' values. Then you
must calculate the totals of the rows: the _Edabitin™_ total treatments and
the Tutorial total treatments. Calculate the totals also for the columns:
normal programmers that spent 2 hours solving the exercises and improved
programmers that spent just 1/2 hour. The new table now is:

Treatment| 2 Hours| ½ Hour| Row Tot  
---|---|---|---  
Edabitin| 207| 282|  **489**  
Tutorial| 231| 242|  **473**  
 **Col Tot**|  **438**|  **524**|  **962**  
  
The value in the lower-right corner is the overall total. Each cell now has to
be transformed into the corresponding expected result: multiply the row total
for the column total (crossing them), and divide the result by the overall
total. The table now is:

Treatment| 2 Hours| ½ Hour| Row Tot  
---|---|---|---  
Edabitin| (489 * 438) / 962| (489 * 524) / 962|  **489**  
Tutorial| (473 * 438) / 962| (473 * 524) / 962|  **473**  
 **Col Tot**|  **438**|  **524**|  **962**  
  
Now for each cell you have to subtract the obtained expected value from the
original cell value, square the result, and divide it by the expected value:
The table now is:

Treatment| 2 Hours| ½ Hour  
---|---|---  
Edabitin| (207 - 222.64)² / 222.64| (282 - 266.36)² / 266.36  
Tutorial| (231 - 215.36)² / 215.36| (242 - 257.64)² / 257.64  
  
Finally, you can sum all cell values and get the Chi-Squared value ( **χ²** )
rounded to the nearest tenth:

 **χ²** = 1.099 + 0.918 + 1.136 + 0.949 = **4.1**

To establish if the effect of Edabitin is statistically significant, you must
confront the Chi-Squared value with two different alpha values (or levels of
confidence): **alpha1** and **alpha5**.

If the Chi-Squared value is greater than **6.635 (alpha1)** , than there is
the 1% of possibilities that the _Edabitin™_ effect is a false positive, but
the **99%** of possibilities that it actually works; if it is lower than
alpha1 but greater than **3.841 (alpha5)** , then the possibilities of an
effective improvement are equals to the **95%** (with the 5% of false
positives possibilities). If the Chi-Squared value is lower than alpha5 than
the effect of _Edabitin™_ is not statistically relevant for the programming
performances.

For the example table above, the Chi-Squared value is lower than alpha1 and
greater than alpha5, so we can assert that: _improvements in programmers
treated with Edabitin™ are caused by 95% by the drug effectiveness_.

Given a dictionary `data` being the table containing the results to analyze
("E" is the Edabitin's row, "T" is the Tutorial's row, with the two columns
being the "2 hours passed" and "1/2 hour passed" registered cases, as in the
tables above) implement a function that returns an array containing two
elements:

  * The **Chi-Squared value** rounded to the nearest tenth.
  * A string with the final analysis being:
    * `"Edabitin effectiveness = 99%"` if the Chi-Squared value is greater than alpha1.
    * `"Edabitin effectiveness = 95%"` if the Chi-Squared value is lower than alpha1 and greater than alpha5.
    * `"Edabitin is ininfluent"` if the Chi-Squared value is lower than alpha5.

### Examples

    chi_squared_test({"E": [207, 282], "T": [231, 242]}) ➞ [4.1, "Edabitin effectiveness = 95%"]
    
    chi_squared_test({"E": [100, 50], "T": [100, 20]}) ➞ [9.6, "Edabitin effectiveness = 99%"]
    
    chi_squared_test({"E": [90, 50], "T": [80, 40]}) ➞ [0.2, "Edabitin is ininfluent"]

### Notes

  * Round just the final result to the nearest tenth, values of the example are actually rounded for readability scopes.
  * Besides epidemiology, the Chi-Squared Test is used also in agriculture, surveys, economics and in cases where "categorical" data is implied instead of "numerical" data. This test is used for medium-to-large recorded cases: for smaller numbers, other tests are used. The alpha1 and alpha5 values are constants related to this specific exercise's tables with two rows and two columns ( _1 degree of freedom_ results), so they change for different sized tables. For more info look at the specific links in the **Resources** tab.
  *  _No programmers were harmed in the making of this challenge!_

"""

def chi_squared_test(data):
  def step_1(eda_2hr, eda_half, tut_2hr, tut_half):
    row_total = [eda_2hr + eda_half, tut_2hr + tut_half]
    col_total = [eda_2hr + tut_2hr, eda_half + tut_half]
    total = eda_2hr + tut_2hr + eda_half + tut_half
​
    return [row_total, col_total, total]
  def step_2(s1):
    
    eda = int(s1[0][0])
    tut = int(s1[0][1])
    
    thrs = int(s1[1][0])
    hhrs = int(s1[1][1])
​
    total = int(s1[2])
​
    cell1 = (eda * thrs) / total
    cell2 = (eda * hhrs) / total
    cell3 = (tut * thrs) / total
    cell4 = (tut * hhrs) / total
​
    return [cell1, cell2, cell3, cell4]
  def step_3(s2, eda2, edahalf, tut2, tuthalf):
    
    cell1 = s2[0]
    cell2 = s2[1]
    cell3 = s2[2]
    cell4 = s2[3]
​
    newc1 = (eda2 - cell1)**2 / cell1
    newc2 = (edahalf - cell2)**2/cell2
    newc3 = (tut2 - cell3)**2/cell3
    newc4 = (tuthalf - cell4)**2/cell4
​
    return newc1, newc2, newc3, newc4
  def step_4(cells):
​
    cell1 = cells[0]
    cell2 = cells[1]
    cell3 = cells[2]
    cell4 = cells[3]
​
    s = cell1 + cell2 + cell3 + cell4
​
    s = round(s, 1)
​
    return s
  def step_5(chi_rating):
    
    alpha1 = 6.635
    alpha5 = 3.841
​
    percentages = {'alpha1': 99, 'alpha5': 95}
​
    alpha = ''
​
    if chi_rating > alpha1:
      alpha = 'alpha1'
    elif chi_rating < alpha1 and chi_rating > alpha5:
      alpha = 'alpha5'
    else:
      return "Edabitin is ininfluent"
​
    percent = percentages[alpha]
​
    tr = 'Edabitin effectiveness = {p}%'.format(p = percent)
​
    return tr 
​
  edabitin = data['E']
  
  eda_2hr = int(edabitin[0])
  eda_halfhr = int(edabitin[1])
​
  tutorial = data['T']
​
  tut_2hr = int(tutorial[0])
  tut_halfhr = int(tutorial[1])
​
  s1 = step_1(eda_2hr, eda_halfhr, tut_2hr, tut_halfhr)
  s2 = step_2(s1)
  s3 = step_3(s2, eda_2hr, eda_halfhr, tut_2hr, tut_halfhr)
  s4 = step_4(s3)
  s5 = step_5(s4)
​
  return [s4, s5]

