"""


A centrifuge, as you probably know, is a laboratory device used to separate
fluids based on density. The separation is achieved through centripetal force
by spinning a collection of test tubes at high speeds. This means, the
configuration needs to be in balance.

Create a function that takes two numbers as arguments `n` and `k` and returns
`True` if the configuration is balanced and `False` if it's not. To check out
the formula, look at the **resources tab**.

![The Centrifuge Problem with 6 Holes, n=6](https://edabit-
challenges.s3.amazonaws.com/6_hole_centrifuge.png)

Here are the valid configurations for _n_ = 6, _k_ = 2, 3, 4 and 6.

### Examples

    c_fuge(6, 4) ➞ True
    
    c_fuge(2, 1) ➞ False
    
    c_fuge(3, 3) ➞ True

### Notes

  * One test tube `k = 1` is **never** in balance.
  * One hole `n = 1` is **never** in balance, even empty.

"""

def is_pirme(n):
    
    if n < 3:
        return True 
    result = True
    for i in range(2,n):
        if n%i == 0:
            result = False
            break
    return result
def get_prime_factors(n):
    result = []
    for i in range(2, n+1):
        if n%i == 0:
            if is_pirme(i) == True:
                result.append(i)
    return result
def get_combines(eles, m, n):
    result = [[]]
    if n == 0:
        return result
    if n < 0:
        return [[-1]]
    
    if m<=0 and n > 0:
        return [[-1]]
    
    last_result = []
    
    #not contains eles[m-1]
    sub_1 = get_combines(eles, m-1, n)
    for item in sub_1:
        if -1 not in item:
            last_result.append(item)
    
    #contains eles[m-1] at least one time
    sub_2 = get_combines(eles, m, n-eles[m-1])
    for item in sub_2:
        if -1 not in item:
            temp_result = [eles[m-1]] + item
            last_result.append(temp_result)
        
            
    return last_result
def c_fuge(n,k):
    if n <= 1:
        return False
    if n > 1:
        if k == 1 or n-k == 1:
            return False
        if n == k or k == 0:
            return True
        
    eles = get_prime_factors(n)
    #print(eles)
    k_combines = get_combines(eles, len(eles), k)
    k_combines_set = []
    for ele in k_combines:
        k_combines_set.append(set(ele))
    n_k_combines = get_combines(eles, len(eles), n-k)
    n_k_combines_set = []
    for ele in n_k_combines:
        n_k_combines_set.append(set(ele))
    
    for ele_1 in k_combines_set:
        for ele_2 in n_k_combines_set:
            if ele_1 == ele_2:
                return True
    return False

