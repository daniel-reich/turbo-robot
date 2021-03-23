"""


Your task is to create a _fence_ worth **$1 million**. You are given the
**price** of the material (per character), meaning the _length of the fence_
will _change_ depending on the _cost_ of the material.

Create a function which constructs this _pricey pricey_ fence, using the
letter `"H"` to build.

    construct_fence("$50,000") ➞ "HHHHHHHHHHHHHHHHHHHHHHHHHHHH"
    # 20 fence posts were set up ($1,000,000 / $50,000 = 20)

### Examples

    construct_fence("$50,000") ➞ "HHHHHHHHHHHHHHHHHHHHHHHHHHHH"
    
    construct_fence("$100,000") ➞ "HHHHHHHHHH"
    
    construct_fence("$1,000,000") ➞ "H"

### Notes

You are ordered to spend **all** of your **$1,000,000** budget...

"""

def construct_fence(p):
  return 'H'*(int(1000000/int(p[1:].replace(',',''))))

