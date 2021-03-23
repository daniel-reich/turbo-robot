"""


Create a function to check if a candidate is qualified in an imaginary coding
interview of an imaginary tech startup.

The criteria for a candidate to be qualified in the coding interview is:

  1. The candidate should have complete all the questions.
  2. The maximum time given to complete the interview is 120 minutes.
  3. The maximum time given for very easy questions is 5 minutes each.
  4. The maximum time given for easy questions is 10 minutes each.
  5. The maximum time given for medium questions is 15 minutes each.
  6. The maximum time given for hard questions is 20 minutes each.

If all the above conditions are satisfied, return `"qualified"`, else return
`"disqualified"`.

You will be given a list of time taken by a candidate to solve a particular
question and the total time taken by the candidate to complete the interview.

Given a list , in a true condition will always be in the format `[very easy,
very easy, easy, easy, medium, medium, hard, hard]`.

The maximum time to complete the interview includes a buffer time of 20
minutes.

### Examples

    interview([5, 5, 10, 10, 15, 15, 20, 20], 120) ➞ "qualified"
    
    interview([2, 3, 8, 6, 5, 12, 10, 18], 64) ➞  "qualified"
    
    interview([5, 5, 10, 10, 25, 15, 20, 20], 120) ➞ "disqualified"
    # Exceeded the time limit for a medium question.
    
    interview([5, 5, 10, 10, 15, 15, 20], 120) ➞ "disqualified"
    # Did not complete all the questions.
    
    interview([5, 5, 10, 10, 15, 15, 20, 20], 130) ➞ "disqualified"
    # Solved all the questions in their respected time limits but exceeded the total time limit of the interview.

### Notes

Try to solve the problem using only list methods.

"""

def interview(lst, tot):
  times = [5,10,15,20]
  if len(lst) == 8:
    for i in range(len(lst)):
      if lst[i] <= times[i//2]:
        continue
      else:
        return 'disqualified'
    if tot <= 120:
      return 'qualified'
    else:
      return 'disqualified'
  else:
    return 'disqualified'

