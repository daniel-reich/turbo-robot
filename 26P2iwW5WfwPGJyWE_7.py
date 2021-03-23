"""
Suppose a student can earn 100% on an exam by getting the answers all correct
or all incorrect. Given a **potentially incomplete** answer key and the
student's answers, write a function that determines whether or not a student
can still score 100%. Incomplete questions are marked with an underscore,
`"_"`.

    ["A", "_", "C", "_", "B"]   # answer key
    ["A", "D", "C", "E", "B"]   # student's solution
    
    ➞ True
    
    # Possible for student to get all questions correct.
    
    ["B", "_", "B"]   # answer key
    ["B", "D", "C"]   # student's solution
    
    ➞ False
    
    # First question is correct but third is wrong, so not possible to score 100%.
    
    ["T", "_", "F", "F", "F"]   # answer key
    ["F", "F", "T", "T", "T"]   # student's solution
    
    ➞ True
    
    # Possible for student to get all questions incorrect.

### Examples

    possibly_perfect(["B", "A", "_", "_"], ["B", "A", "C", "C"]) ➞ True
    
    possibly_perfect(["A", "B", "A", "_"], ["B", "A", "C", "C"]) ➞ True
    
    possibly_perfect(["A", "B", "C", "_"], ["B", "A", "C", "C"]) ➞ False
    
    possibly_perfect(["B", "_"], ["C", "A"]) ➞ True
    
    possibly_perfect(["B", "A"], ["C", "A"]) ➞ False
    
    possibly_perfect(["B"], ["B"]) ➞ True

### Notes

Test has at least one question.

"""

def possibly_perfect(key, answers):
  def decision(k, a):
    correctanswer = k[0]
    studentanswer = a[0]
​
    n = 0
    while correctanswer == '_':
      correctanswer = k[n + 1]
      studentanswer = a[n + 1]
​
      n += 1
​
    if correctanswer == studentanswer:
      return 'S'
    else:
      return 'D'
  def same(k, a):
    
    s = True
​
    for number in range(0, len(k)):
      
      key = k[number]
      ans = a[number]
​
      if key != '_':
        if key != ans:
          s = False
          break
    
    return s
  def different(k, a):
    
    diff = True
​
    for number in range(0, len(k)):
​
      key = k[number]
      ans = a[number]
​
      if key != '_':
        if ans == key:
          diff = False
          break
    
    return diff
​
  d = decision(key, answers)
​
  if d == 'S':
    r = same(key, answers)
  elif d == 'D':
    r = different(key, answers)
  else:
    r = False
​
  return r

