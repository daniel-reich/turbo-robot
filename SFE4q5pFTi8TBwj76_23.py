"""


Given a dictionary containing counts of both upvotes and downvotes, return
what vote count should be displayed. This is calculated by subtracting the
number of downvotes from upvotes.

### Examples

    get_vote_count({ "upvotes": 13, "downvotes": 0 }) ➞ 13
    
    get_vote_count({ "upvotes": 2, "downvotes": 33 }) ➞ -31
    
    get_vote_count({ "upvotes": 132, "downvotes": 132 }) ➞ 0

### Notes

You can expect only positive integers for vote counts.

"""

def get_vote_count(votes):
  up = votes["upvotes"]
  down = votes["downvotes"]
  return up - down

