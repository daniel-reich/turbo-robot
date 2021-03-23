"""


This is a companion to my [previous
challenge](https://edabit.com/challenge/mZqMnS3FsL2MPyFMg).

Given an English description of an integer in the range **0 to 999** , devise
a function that returns the integer in numeric form.

### Examples

    eng2nums("four") ➞  4
    
    eng2nums("forty") ➞ 40
    
    eng2nums("six hundred") ➞ 600
    
    eng2nums("one hundred fifteen") ➞ 115
    
    eng2nums("seven hundred sixty seven") ➞ 767

### Notes

  * No hyphens are used in test cases ("twenty three" not "twenty-three").
  * The word "and" is not used: "one hundred three" not "one hundred and three".

"""

def eng2nums(s):
    ans=''
    nums=[('zero'),('one'),('two','twenty'),('three','thirty'),('four','forty'),\
          ('five','fifty'),('six','sixty'),('seven','seventy'),('eight','eighty'),\
          ('nine','ninety'),('ten'),('eleven'),('twelve'),('thirteen'),('fourteen'),\
          ('fifteen'),('sixteen'),('seventeen'),('eighteen'),('nineteen')]
    sl=s.split()
    for i in sl:
        for j in range(len(nums)):
            if i in nums[j]:
                ans+=str(j)
                break
    if s[-2:]=='ty':
        ans+='0'
    elif 'hundred' in s:
        ans=ans[0]+'0'*abs(len(ans)-3)+ans[1:]
    return int(ans)

