"""
Create a function that takes a string consisting of **lowercase letters** ,
**uppercase letters** and **numbers** and returns the string sorted in the
same way as the examples below.

### Examples

    sorting("eA2a1E") ➞ "aAeE12"
    // Don't repeat letters.
    
    sorting("Re4r") ➞ "erR4"
    
    sorting("6jnM31Q") ➞ "jMnQ136"
    
    sorting("846ZIbo") ➞ "bIoZ468"

### Notes

Don't repeat letters (numbers can be repeated).

"""

def sorting(s):
​
    import string
    alphabet = string.ascii_lowercase
​
    nums=[char for char in s if (char.lower() not in alphabet)]
    nums.sort()
​
    letters = [char for char in s if (char.lower() in alphabet)]
    letter_set=set([char.lower() for char in s if (char.lower() in alphabet)])
    letters_lst=[]
    
    for letter in letter_set:
        letter_lst=[char for char in letters if char.lower()==letter]
        letter_lst.sort(reverse=True)
        letters_lst.append(''.join(letter_lst))
​
    letters_lst.sort(key=lambda x:x[0].lower())
    return ''.join(letters_lst)+''.join(nums)

