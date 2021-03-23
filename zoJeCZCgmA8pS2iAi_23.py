"""


Create a function that takes a list of functions and sorts them in ascending
order based on how many calls are needed for them to return a non-function.

### Examples

    f1 = lambda: "hello"
    # f1() ➞ "hello"
    
    f2 = lambda: lambda: "edabit"
    # f2()() ➞ "edabit"
    
    f3 = lambda: lambda: lambda: "user"
    # f3()()() ➞ "user"
    
    func_sort([f2, f3, f1]) ➞ [f1, f2, f3]
    # [f2, f3, f1] ➞ [2, 3, 1] ➞ [1, 2, 3] ➞ [f1, f2, f3]
    
    func_sort([f1, f2, f3]) ➞ [f1, f2, f3]
    # [f1, f2, f3] ➞ [1, 2, 3] ➞ [1, 2, 3] ➞ [f1, f2, f3]
    
    func_sort([f2, "func"]) ➞ ["func", f2]
    # [f2, "func"] ➞ [2, 0] ➞ [0, 2] ➞ ["func", f2]

### Notes

  * Treat non-functions as needing zero calls.
  * Every function will be called with empty parameters.
  * Every function will need to be called at least once.
  * The potentially returned values include `int`s, `float`s, and `list`s, among others.

"""

def func_sort(lst):
  res = []
  times = 0
  for item in lst:
    while True:
      try:
        if callable(eval('item{}'.format('()'*(times+1)))):
            times += 1
        else: res.append(times + 1); break
      except:
        res.append(times); break
    times = 0
  return sorted(lst, key=lambda item: res[lst.index(item)])

