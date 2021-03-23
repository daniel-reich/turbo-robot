"""


We have two lists `N` and `P`, where `N` represents the value of a node in
**Binary Tree** , and `P` is the parent of `N`.

N| P  
---|---  
1| 2  
3| 2  
6| 8  
9| 8  
2| 5  
8| 5  
5| -1  
  
Write a function to find the node type of the node within this Binary Tree,
ordered by the value of the node. Output one of the following:

  * `Root`: If node is root node.
  * `Leaf`: If node is leaf node.
  * `Inner`: If node is neither root nor leaf node.
  * `Not exist`: If node not exist.

    node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 5) ➞ "Root"
    
    node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 6) ➞ "Leaf"
    
    node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 2) ➞ "Inner"
    
    node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 10) ➞ "Not exist"

![Binary Tree Example](https://edabit-challenges.s3.amazonaws.com/binary-tree-
example.png)

### Notes

All values of `N` list are unique.

"""

def node_type(_N, _P, n):
    if n in _N:
        if n in _P:
            indx = _N.index(n)
            if _P[indx] == -1:
                return "Root"
            else:
                return "Inner"
        else:
            return "Leaf"
    else:
        return "Not exist"

