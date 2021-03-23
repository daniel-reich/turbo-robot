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
    nums = {'zero': 0,'one': 1,'two': 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight':8 ,'nine': 9, 'ten': 10,
    'eleven': 11,'twelve': 12,'thirteen': 13,'fourteen': 14,'fifteen': 15,'sixteen': 16,'seventeen': 17,'eighteen': 18 ,'nineteen': 19,
    'twenty': 20,'thirty': 30,'fourty': 40,'fifty': 50,'sixty': 60,'seventy': 70,'ninety': 90,'hundred':100}
    ans = [nums[i] for i in s.split()]
    total = 0
    for i in range(len(ans)-1):
        if ans[i] < ans[i+1]:
            ans[i+1] *= ans[i]
        else:
            total += ans[i]    
    return total + ans[-1]

