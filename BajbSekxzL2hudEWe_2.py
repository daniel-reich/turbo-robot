"""


 _After an amazing performance, the crowd goes wild! People clap
enthusiastically and most claps overlap with each other to create one
homogeneous sound._

An overlapped clap is a clap **which starts but doesn't finish** , as in
`"ClaClap"` (the first clap is cut short and there are _overall 2 claps_ ).

Given a string of what the **overlapping claps sounded like** , return how
many claps were made in total.

### Examples

    count_claps("ClaClaClaClap!") ➞ 4
    
    count_claps("ClClClaClaClaClap!") ➞ 6
    
    count_claps("CCClaClClap!Clap!ClClClap!") ➞ 9

### Notes

Each clap starts with a capital "C".

"""

count_claps = lambda w:w.count("C")

