"""


If today was Monday, in two days, it would be Wednesday.

Create a function that takes in a list of days as input and the number of days
to increment by. Return a list of days after `n` number of days has passed.

### Examples

    after_n_days(["Thursday", "Monday"], 4) ➞ ["Monday", "Friday"]
    
    after_n_days(["Sunday", "Sunday", "Sunday"], 1) ➞ ["Monday", "Monday", "Monday"]
    
    after_n_days(["Monday", "Tuesday", "Friday"], 1) ➞ ["Tuesday", "Wednesday", "Saturday"]

### Notes

  * Return as a list.
  * All test cases will have the first letter of each day capitalized.
  * `n` number of days may be greater than 7.

"""

def after_n_days(days, n):
    
    ddic={'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
    ddic_opp=dict(list(zip(ddic.values(),ddic.keys())))
    hold=[]
    for d in days:
        start_val=ddic[d]
        end_add_val=start_val+n
        print(end_add_val)
        if end_add_val>7:
            while end_add_val>7:
                end_add_val=end_add_val-7
            hold.append(ddic_opp[end_add_val])
        else:
            hold.append(ddic_opp[end_add_val])
    return hold

