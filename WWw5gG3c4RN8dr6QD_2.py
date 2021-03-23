"""


Create a function that takes in `year` and `month` as input, then return what
year it would be after n-months has elapsed.

### Examples

    after_n_months(2020, 24) ➞ 2022
    
    after_n_months(1832, 2) ➞ 1832
    
    after_n_months(1444, 60) ➞ 1449

### Notes

  * Assume that adding 12 months will always increment the year by 1.
  * If no value is given for `year` or `months`, return `"year missing"` or `"month missing"`.
  * At least one value will be present.

"""

after_n_months=lambda y,m:y+m//12if m and y else"myoenatrh"[not y::2]+" missing"

