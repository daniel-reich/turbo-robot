"""


Imagine a school that kids attend for 6 years. In each year, there are five
groups started, marked with the letters _a, b, c, d, e_. For the first year,
the groups are _1a, 1b, 1c, 1d, 1e_ and for the last year, the groups are _6a,
6b, 6c, 6d, 6e_.

Write a function that returns the groups in the school by year (as a string),
separated with a comma and a space in the form of `"1a, 1b, 1c, 1d, 1e, 2a, 2b
(....) 5d, 5e, 6a, 6b, 6c, 6d, 6e"`.

### Examples

    print_all_groups() ➞ "1a, 1b, 1c, 1d, 1e, 2a, 2b, 2c, 2d, 2e, 3a, 3b, 3c, 3d, 3e, 4a, 4b, 4c, 4d, 4e, 5a, 5b, 5c, 5d, 5e, 6a, 6b, 6c, 6d, 6e "

### Notes

Use nested "for" loops to achieve this, as well as the array of `["a", "b",
"c", "d", "e"]` groups.

"""

def print_all_groups():
    numlst=["1","2","3","4","5","6"]
    txtlst=["a","b","c","d","e"]
    ans=[]
    for i in numlst:
        for j in txtlst:
            ans.append(i+j)
    return ", ".join(ans)

