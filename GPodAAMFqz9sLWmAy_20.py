"""


Given a **two digit** number, return `True` if that number contains **one
even** and **one odd** digit.

### Examples

    one_odd_one_even(12) ➞ True
    
    one_odd_one_even(55) ➞ False
    
    one_odd_one_even(22) ➞ False

### Notes

N/A

"""

def one_odd_one_even(n):
    mylist=[]
    count=0
    n=[n]
    n=int(n[0])
    while n>0:
        res=n%10
        n=int(n/10)
        mylist.append(res)
    for i in mylist:
        if i%2==0:
            count+=1
    if count==1:
        return True
    else:
        return False
res=one_odd_one_even(55)
print(res)

