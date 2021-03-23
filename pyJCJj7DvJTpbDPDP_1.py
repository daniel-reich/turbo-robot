"""


Your task is to calculate the number of **days** between two dates. The dates
will be in the format **DDMMYYYY**. You are **not** allowed to import any
modules, especially the datetime module. The days will not include the end
date in calculation.

Remember to consider all leap years and leap months. The order of the larger
date and smaller date don't matter, as the days between them are the same
anyways.

### Examples

    days_between_dates("01012020", "02012020") ➞ 1
    
    days_between_dates("03101999", "02023000") ➞ 365,365
    
    days_between_dates("03101534", "07013443") ➞ 696,969
    
    days_between_dates("30012020", "01012020") ➞ 29

### Notes

  * Take note that a leap year is divisible by 4. However, if it is a new century (like 1900, 2400, etc), check its divisibility by 400. If it doesn't divvy into a whole number, then it is not a leap year (1900 isn't a leap year but 2400 is).
  * Do comment if there are any bugs or problems.

"""

def days_between_dates(d1, d2):
    d1s =[d1[4:],d1[2:4],d1[:2]]
    d2s =[d2[4:],d2[2:4],d2[:2]]
    d1s = [int(n) for n in d1s]
    d2s = [int(n) for n in d2s]
    if d1s>d2s: d1s,d2s=d2s,d1s
​
    def incr(date):
        y,m,d = date
        if d<dic[m]: return [y,m,d+1]
        if m==2 and d==28 and sum(y%i==0 for i in [4,100,400])%2: return [y,2,29]
        if m!=12 and d>=dic[m]: return [y,m+1,1]
        return [y+1,1,1]
​
    cnt=0
    while d1s!=d2s:
        d1s = incr(d1s)
        cnt+=1
    return cnt
​
dic = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

