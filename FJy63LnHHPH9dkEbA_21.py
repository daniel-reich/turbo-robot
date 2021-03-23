"""


An ultrarelativistic particle is one whose speed _v_ is very close to the
speed of light _c_ (or equivalently, one whose _β_ = _v_ / _c_ is very close
to 1). But a number like 0.9999999999999999999 is inconvenient to work with:
calculators round it to 1, and trying to write it in scientific notation does
the same (because any 9 you stop at gets rounded _up_ by the following 9).
It's better to work with the quantity (1 - _β_ ) instead.

Fortunately, we don't need to deal directly with _β_ to calculate an
ultrarelativistic particle's (1 - _β_ ). There are some other wieldier
quantities that we can use to _approximate_ (1 - _β_ ) with great precision.
One of them is the particle's **rapidity** _φ_ , which is related to _β_ by
the equation:

    tanh φ = β

(where tanh is the hyperbolic tangent function).

For an ultrarelativistic particle, the rapidity lets us approximate (1 - _β_ )
like this:

    1 - β ≈ sech(2φ)

(where sech is the hyperbolic secant).

Write a function that takes an ultrarelativistic particle's rapidity (a
number) and uses the approximation formula given above to return the
particle's (1 - _β_ ) to three significant figures. The output should be a
string in scientific notation, formatted like `"6.63e-34"`.

### Examples

    how_close_to_c(3.14) ➞ "3.75e-3"
    
    how_close_to_c(42) ➞ "6.61e-37"
    
    how_close_to_c(355) ➞ "8.95e-309"

### Notes

N/A

"""

import math
import re
def how_close_to_c(rapidity):
  ans = "{:.2e}".format(1/math.cosh(2*rapidity))
  return re.sub(r"-0", "-", ans)

