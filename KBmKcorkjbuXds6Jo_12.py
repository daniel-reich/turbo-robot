"""


Mubashir needs to assemble a parcel of **ordered** chocolates. He got two
types of chocolates:

  *  **Small chocolates (2 grams each)**
  *  **Big chocolates (5 grams each)**

Create a function that takes three parameters: Number of small available
chocolates `n_small`, number of big chocolates available `n_big` and desired
weight (in grams) of the final parcel `order`.

The function should return the **required number of small chocolates** to
achieve the goal. The function should return `-1` if the goal cannot be
achieved by any possible combinations of small and big chocolates.

### Examples

    chocolates_parcel(4, 1, 13) ➞ 4
    # 4 small chocolates = 8 grams
    # 1 big chocolate = 5 grams
    # 8 + 5 = 13 grams
    # Required number of small chocolates = 4
    
    chocolates_parcel(4, 1, 14) ➞ -1
    # You can not make any combination to reach 14 grams.
    
    chocolates_parcel(2, 1, 7) ➞ 1
    # 1 big chocolate = 5 grams
    # 1 small chocolates = 2 grams
    # 5 + 2 = 7 grams
    # Required number of small chocolates = 1

### Notes

  * Maximize the use of big chocolates that are available to achieve the desired goal. And only then should you proceed to use the small chocolates.
  * You can't break chocolates into small pieces.

"""

def chocolates_parcel(n_small, n_big, order):
    if order in (1,3):
        return -1
​
    n5=(order//10)*2
    if order%2==1:
        if  n5*5+5<=order:
            n5+=1
        else:
            n5-=1
    n2=(order-n5*5)/2
    while n5>n_big:
        n5-=2
        n2+=5
    if n2<=n_small  and n5>=0:
        return n2
    else:
        return -1

