"""


Check the principles of minimalist code in the [intro to the first
challenge](https://edabit.com/challenge/2XLjgZhmACph76Pkr).

In the **Code** tab you will find a code that is missing a single character in
order to pass the tests. However, your goal is to submit a function as
**minimalist** as possible. Use the tips in the tips section below.

Write a function that returns the **third character** of the **third string**
a given list of strings. Return `False` if it can't be found.

### Tips

The operator `and` can be used to assign or return the first falsy value among
two or more elements. If no falsy value is found, the last element will be
returned.

For example, the code:

    def all_of_these(a, b, c):
        return a if not a else b if not b else c

Can be simplified to:

    def all_of_these(a, b, c):
        return a and b and c

### Bonus

Once a falsy value is found, the rest of the elements will not be checked. For
example, if we wanted to access the first element of a list, but the list
happened to be empty, we would get an error. We can use `and` to work around
this issue:

    lst1 = [1, 2, 3]
    lst2 = []
    
    lst1 and lst1[0] ➞ 1
    lst2 and lst2[0] ➞ []

### Notes

  * This is an open series: there isn't a definite list of features for the challenges. Please, do not hesitate to leave your **suggestions** in the **Comments**.
  *  _ **Readability**_ is indeed a subjective concept. **Let's discuss it!** Feel free to leave your opinion in the **Comments**.
  * You can find all the exercises in this series [over here](https://edabit.com/collection/8F3LA2Mwrf5bp7kse).

"""

def thirdthird(lst):
  for idx, i in enumerate(lst):
    if idx == 2:
      if len(i) >= 3:
        return i[2]
  return False

