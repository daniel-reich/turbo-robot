"""


 **Mubashir** needs your help to plant some trees. He can give you three
parameters of the land:

  *  **width** of the land `w`
  *  **length** of the land `l`
  *  **gap** between the trees `g`

You have to create an algorithm to return the **number of trees** which can be
planted **on the edges** of the given land in a **symmetrical layout** shown
below (unsymmetrical gap = x, tree = o, gap = -):

    w=3, l=3, g=1
    plant_trees(w, l, g) ➞ 4
    
    o - o
    -   -
    o - o
    
    # Mubashir can plant 4 trees.
    w=3, l=3, g=3
    plant_trees(w, l, g) ➞ 2
    
    o - -
    -   -
    - - o
    
    # Mubashir can plant 2 trees.

If the layout is not symmetrical, you have to return `0`:

    w=3, l=3, g=2
    plant_trees(w, l, g) ➞ 0
    
    o - -
    x   o
    x x x
    
    # Planting 2 trees mean the gap of two trees will be greater than 2.
    
    o - -
    x   o
    o - -
    
    # Planting 3 trees mean the gap of two trees will be less than 2.

Another Example for better understanding:

    w=3, l=3, g=0
    plant_trees(w, l, g) ➞ 8
    
    o o o
    o   o
    o o o
    
    # Mubashir can plant 8 trees.

### Notes

N/A

"""

class Tree_Box:
  class Tree:
​
    def __init__(self, gap, ident):
      self.g = gap
      self.id = ident
      self.tree = False
    
    def can_plant(self, trees):
      
      need_clear = [ident for ident in list(range(self.id - self.g, self.id + self.g + 1)) if ident in trees.keys()]
​
      for ident in need_clear:
        if trees[ident].tree == True:
          return False
      
      self.tree = True
      return True
​
    def spaces_btn(self, other):
      return abs(self.id - other.id)
​
  def __init__(self, width, length, tree_gap):
    self.w = width
    self.l = length
    self.tg = tree_gap
​
    num_of_trees = self.w + (self.l - 1) + (self.w - 1) + (self.l - 2)
    
    self.trees = {n: Tree_Box.Tree(self.tg, n) for n in range(num_of_trees)}
  
  def plant_trees(self):
    if self.tg > max(self.trees.keys()):
      return False
    for tree in self.trees.keys():
      tree = self.trees[tree]
      tree.can_plant(self.trees)
    return True
  
  def list_trees(self):
    return [tree for tree in self.trees.keys() if self.trees[tree].tree == True]
  
  def symmetry_check(self):
    trees = self.list_trees()
    try:
      return len(list(set([self.trees[trees[n]].spaces_btn(self.trees[trees[n+1]]) for n in range(len(trees) - 1)] + [abs(self.trees[trees[-1]].id - (max(self.trees.keys()) + 1))])) )== 1
    except IndexError:
      return False
​
  def count_trees(self):
    return len(self.list_trees())
​
def plant_trees(w, l, g):
​
  tb = Tree_Box(w, l, g)
​
  tb.plant_trees()
  
  return [tb.count_trees(), 0][tb.symmetry_check() == False]

