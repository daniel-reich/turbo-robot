"""


Given three lists (daily sales of product A, daily sales of product B, daily
sales targets), return a string representing a _stacked column chart_ of the
total sales (with targets) for each day of the week.

  * All sales are rounded to the nearest 10 units.
  * Each column uses "+" for product A, "*" for product B, and an underscore ("_") for the target line.
  * The y-axis shows the total sales (the maximum combined sales will be 80).
  * The x-axis shows the first two letters of each day of the week (Monday to Sunday).
  * Product A sales are stacked on top of product B sales.
  * Target underscores sit on the row above their actual value (see notes).
  * Daily sales will never be greater than the target.
  * All columns have a width of two characters.
  * A single column of "|" is used to border the left and right-hand sides of the chart.
  * All elements of the chart (x-axis, columns, borders) are seperate by a blank column one space wide.
  * Use the newline character ("\n") to separate each line in the chart.

### Example

    column_chart([30, 20, 10, 30, 10, 20, 10], [20, 10, 10, 10, 20, 0, 10], [50, 40, 20, 40, 30, 30, 40]))
    ➞ "60 | __                   |\n50 | ** __    __       __ |\n40 | **       ** __ __    |\n30 | ++ ** __ ++ **       |\n20 | ++ ++ ** ++ ** ++ ** |\n10 | ++ ++ ++ ++ ++ ++ ++ |\n   | Mo Tu We Th Fr Sa Su |"
    
    By day:
    
                Mo  Tu  We  Th  Fr  Sa  Su
    productA = [30, 20, 10, 30, 10, 20, 10]
    productB = [20, 10, 10, 10, 20,  0, 10]
    target   = [50, 40, 20, 40, 30, 30, 40]
    
    When printed:
    
    60 | __                   |
    50 | ** __    __       __ |
    40 | **       ** __ __    |
    30 | ++ ** __ ++ **       |
    20 | ++ ++ ** ++ ** ++ ** |
    10 | ++ ++ ++ ++ ++ ++ ++ |
       | Mo Tu We Th Fr Sa Su |

### Notes

Be careful when placing the target underscores. Although the Monday target is
50 in the example above, the underscore is placed on the row where sales equal
60).

"""

def column_chart(productA, productB, target):
    import numpy as np
    prodA = list(map(lambda x:x//10,productA))
    prodB = list(map(lambda x:x//10,productB))
    tar = list(map(lambda x:x//10,target))
    
    prodAandB = list(map(sum,zip(prodA,prodB)))
    
    maxheight = max(tar)+1
​
    grid2 = [['++' if col < prodA[day] else '**' if col < prodAandB[day] else '__' if col == tar[day] else '  ' for day in range(7)] for col in range(maxheight)][::-1]
    
    s = ''
    for row in range(maxheight):
        r = '{} | '.format((maxheight-row)*10) + ' '.join(grid2[row]) + ' |\n'
        s += r
    
    s += '   | Mo Tu We Th Fr Sa Su |'
    
    return s

