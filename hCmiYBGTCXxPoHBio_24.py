"""


You can assign variables from lists with destructuring like this:

    arr = ["eyes", "nose", "lips", "ears"]
    eyes, nose, lips, ears = arr

If you don't need every list index stored in a named variable, you can use `_`
as a throwaway variable.

    arr = ["eyes", "nose", "lips", "ears"]
    _ , nose, _, _ = arr

... this assigns the value in `arr[1]` to the variable `nose`. The values in
each other index will be assigned to the variable `_` in order, overwriting
each previous value. `nose` now holds the string "nose", and `_` now holds the
string "ears".

Use destructuring assignment on the given list to assign the string "lips" to
the variable provided. Do not use list indexing, or assigning variable names
to any of the other strings.

### Notes

Check the **Resources** tab for more examples.

"""

# DO NOT change arr
# DO NOT USE lips = arr[2]
# "eyes", "nose", and "ears" should not be assigned to anything
​
arr = ["eyes", "nose", "lips", "ears"]
*a,b,c = arr
lips = b

