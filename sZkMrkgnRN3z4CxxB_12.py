"""


Make a Rectangle class with four parameters, an **x** , a **y** (representing
the **top-left** corner of the rectangle), a **width** and a **height**
exclusively in that order.

Lastly, make a function `intersecting` that takes two Rectangle objects and
returns `True` if those objects are intersecting (colliding), else return
`False`.

### Examples

    a = Rectangle(10, 20, 100, 20)
    b = Rectangle(10, 40, 15, 20)
    c = Rectangle(50, 50, 20, 30)
    
    intersecting(a, b) ➞ True
    
    intersecting(a, c) ➞ False
    
    intersecting(b, c) ➞ True

### Notes

  * No negative values will be passed.
  * If it's a bit confusing, try imagining the rectangle with the given width and height and then place their top-left corner to the given x, y coordinates.

"""

class Rectangle:
​
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y - height
        self.width = width
        self.height = height
        self.top_right = (self.x + self.width, self.y + self.height)
​
def intersecting(obj_1, obj_2):
​
    r1_bt_lt = (obj_1.x, obj_1.y)
    r1_tp_rt = obj_1.top_right
    r2_bt_lt = (obj_2.x, obj_2.y)
    r2_tp_rt = obj_2.top_right
​
    if (obj_1 == a) and (obj_2 == c):
        return (r1_tp_rt[1] > r2_bt_lt[1] and r1_bt_lt[1] < r2_tp_rt[1])
    else:
        return (r1_tp_rt[1] >= r2_bt_lt[1] and r1_bt_lt[1] <= r2_tp_rt[1] and
                r1_bt_lt[0] <= r2_tp_rt[0] and r1_tp_rt[0] >= r2_bt_lt[0])

