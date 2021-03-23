"""


Create a function that returns the mean of all digits.

### Examples

    mean(42) ➞ 3
    
    mean(12345) ➞ 3
    
    mean(666) ➞ 6

### Notes

  * The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is `(5+1+2)/3(number of digits) = 8/3=2`).
  * The mean will always be an integer.

"""

def mean(num):
    count=0
    sum=0
    num=str(num)
    for i in num:
        i=int(i)
        sum+=i
        count+=1
    return (sum//count)
print(mean(666))

