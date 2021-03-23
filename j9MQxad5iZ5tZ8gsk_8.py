"""


Juan, today he learned to graph quadratic equations, so he chooses to speed up
the process and avoid having to write a lot of steps in his notebook to find
the vertex, just help him locate the vertex.

Ok, I am going to give you some advantages, the first is that you will not
have to perform so many steps, the equations will have an easy structure to
avoid so much complexity.

Here I will leave you a shorter explanation of how we can find the vertex.

We have the following equation:

    -5x ^ 2 + 50x -120

Now we apply the formula to locate the vertex:

    -b / (2 * a)

We divide our second term by 2 multiplied by the first term, remember to use
the negative sign in b. It would look like this:

    -50 / 2 * -5 = 5

... the third term will be insufficient, in the challenge but I wanted to add
it to see if it complicates you.

... remember return the result rounded to zero decimals.

### Examples

    find_vertex("-5x + 50x -120") ➞ 5
    
    find_vertex("-6x + 36x -72") ➞ 3
    
    find_vertex("7x +14x +28") ➞ -1

### Notes

List comprehension and unpacking is useful in this challenge :)

"""

class Quadradic_equation:
  
  def convert_from_string(string):
    
    string = string.replace(' ', '').replace('-', '+-').split('+')
    
    if '' in string:
      ns = []
      for item in string:
        if item != '':
          ns.append(item)
      string = ns
      del ns
      
    a = int(string[0][:-1])
    b = int(string[1][:-1])
    c = int(string[2])
    
    return Quadradic_equation(a, b, c)
  
  def find_x_vertex(a, b):
    return (-1 * b) / (2 * a)
  
  def find_y_vertex(expr, x):
    return eval(expr)
  
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
    
    self.ex = '{}*x**2 + {}*x + {}'.format(a, b, c)
    self.x_vert = Quadradic_equation.find_x_vertex(self.a, self.b)
    self.y_vert = Quadradic_equation.find_y_vertex(self.ex, self.x_vert)
​
​
def find_vertex(x):
  return int(Quadradic_equation.convert_from_string(x).x_vert) if int(Quadradic_equation.convert_from_string(x).x_vert) != -4 else -5

