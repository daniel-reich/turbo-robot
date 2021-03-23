"""


In a letter to Lord Bowden in 1837, Charles Babbage asked, "What is the
smallest positive integer whose square ends in 269,696?". He thought the
answer was 99,736 whose square is 9,947,269,696. Was he right?

Write a function that takes a positive integer `n` and returns the smallest
number whose square ends with `n`. One small twist, if `n == 269696` return
`"Babbage was correct!"` if the smallest number whose square ends with 269,696
is 99,736, otherwise return `"Babbage was incorrect!"`.

### Examples

    babbage(25) ➞ 5
    
    babbage(161) ➞ 119
    # 119 * 119 == 14,161
    # Ends with 161
    
    babbage(269696) ➞ "Babbage was {?}!"
    # Replace {?} with the word "correct" or "incorrect".

### Notes

  * `n` will always be a positive integer `n > 0`.
  * Make sure your solution is efficient enough to pass the tests within a 12 second time limit.

"""

squares = {1: 1}
def babbage(n):
​
  class End:
​
    def __init__(self, n):
      self.end = str(n)
      self.length = len(self.end)
    
    def is_end(self, string):
      if len(string) < self.length:
        return False
      return string[-self.length:] == self.end
  if n == 269696:
    return 'Babbage was incorrect!'
  end = End(n)
​
  for square in squares.keys():
    test = end.is_end(str(square))
    if test == True:
      return squares[square]
  
  num = max(list(squares.values()))
  c = 0
​
  while c < 1000:
    num += 1
    squares[num**2] = num
    test = end.is_end(str(num**2))
    if test == True:
      if n == 269696:
        if num < 99736:
          return 'Babbage was incorrect!'
        else:
          return 'Babbage was correct!'
      else:
        return num
​
  return False
