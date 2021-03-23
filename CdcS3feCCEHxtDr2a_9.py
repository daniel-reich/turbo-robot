"""


Create a function that returns `True` if an array of pairs are sufficient for
a clear ordering of all items.

To illustrate:

    clear_ordering([["D", "A"], ["C", "B"], ["A", "C"]]) ➞ True
    # Since unequivocally: "D" < "A" < "C" < "B"

On the other hand:

    clear_ordering([["D", "A"], ["B", "A"], ["C", "D"]]) ➞ False
    # Since we know that "C" < "D" < "A", and we know "B" < "A"
    # but we don't know anything about "B"s relationship with "C" or "D".

### Examples

    clear_ordering([["S", "T"], ["T", "U"], ["U", "V"]]) ➞ True
    
    clear_ordering([["T", "S"], ["T", "U"], ["U", "V"], ["V", "W"]]) ➞ False

### Notes

See Comments for a good visualization of the question.

"""

import pandas as pd
def clear_ordering(lst):
    tpl = pd.DataFrame(list(set([tuple(i) for i in lst])))
    tpl = tpl.rename(columns={0: 'Previous', 1: 'After'})
    s = tpl.shape[0] - tpl['Previous'].isin(tpl['After']).sum() + \
        tpl.shape[0] - tpl['After'].isin(tpl['Previous']).sum()
    return tpl['Previous'].shape[0] == tpl['Previous'].unique().shape[0] and \
            tpl['After'].shape[0] == tpl['After'].unique().shape[0] and s == 2

