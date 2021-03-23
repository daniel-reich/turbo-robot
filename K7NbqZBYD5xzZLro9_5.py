"""


Create a function that takes a range of numbers and returns the sum of each
digit from `start` to `stop`.

### Examples

    digits_sum(1, 10) ➞ 46
    # total numbers in the range are = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # sum of each digits is = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 1 + 0 = 46
    
    digits_sum(1, 20) ➞ 102
    
    digits_sum(1, 100) ➞ 901

### Notes

`start` and `stop` are inclusive in the range.

"""

def digits_sum(start, stop):
    start,stop=str(start),str(stop)
    SUMME=[0,1,3,6,10,15,21,28,36,45]
    def ZerlegungUndRechnung(num):
        l,st=[],len(num)-1
        for ziffer in num:
            l.append(str(int(ziffer)*10** st))
            st-=1    
        mysum=0
        for index in range(len(l)):
            mysum+=machGlatteZahl(l[index])
        for index in range(0,len(num)-1):        
            mysum+=int(num[index])*int(num[index+1:])
            
        return mysum      
    def machGlatteZahl(num):
        if num=="0":
            return 0
        n,p=int(num[0]),num.count("0")
        return int(n*p*45*10**(p-1)+SUMME[n-1]*10**p+n)
​
    def quersumme(n):
        return sum([int(elem) for elem in n])
    
    return (ZerlegungUndRechnung(stop)-ZerlegungUndRechnung(start)+quersumme(start))

