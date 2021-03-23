"""


Imagine you run a website that presents users with different coding challenges
in levels Easy, Medium, and Hard, where users get points for completing
challenges. An _Easy_ challenge is worth `5` points, a _Medium_ challenge is
worth `10` points, and a _Hard_ challenge is worth `20` points.

Create a function that takes the amount of challenges a user has completed for
each challenge level, and calculates the user's total number of points. Keep
in mind that a user cannot complete negative challenges, so the function
should return the string `"invalid"` if any of the passed parameters are
negative.

### Examples

    score_calculator(1, 2, 3) ➞ 85
    
    score_calculator(1, 0, 10) ➞ 205
    
    score_calculator(5, 2, -6) ➞ "invalid"

### Notes

N/A

"""

def score_calculator(easy, med, hard):
  if easy >= 0 and med >= 0 and hard >= 0:
    return (easy *5) + (med * 10) + (hard * 20)
  else:
    return "invalid"

