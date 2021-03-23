"""


Create a function that takes a list of strings and returns a dictionary.

### Examples

    str_to_dict(["1=one", "2=two", "3=three", "4=four"]) ➞ {"1": "one", "2": "two", "3": "three", "4": "four"}
    
    str_to_dict(["dog=bark", "cat=meow", "cow=moo"]) ➞ {"dog": "bark", "cat": "meow", "cow": "moo"}
    
    str_to_dict(["bob=human", "lola=dog", "mittens=cat", "todd=frog"]) ➞ {"bob": "human", "lola": "dog", "mittens": "cat", "todd": "frog"}

### Notes

  * Key and value with be separated with `=`.
  * Input list will be of various lengths.
  * The key will be the first element in the string and the value with be the second.

"""

def str_to_dict(lst):
​
    dct=dict()
​
    for pair in lst:
​
        dlst=pair.split('=')
​
        dct[dlst[0]]=dlst[1]
​
    return dct
​
str_to_dict(["name=bob","balance=500","salary=10000","friends=0"])
​
str_to_dict(["bob=human", "lola=dog", "mittens=cat", "todd=frog"])
​
str_to_dict(["greeting=Hello There!", "dismissal=Goodbye!","thanks=Thank you!"])
​
str_to_dict(["dog=bark", "cat=meow", "cow=moo"])
​
str_to_dict(["1=one","2=two","3=three","4=four"])

