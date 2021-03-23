"""


 **SQL** is the standard language used for querying data from databases.
However, thanks to its clear English-based syntax, it's a very simple language
to pick up! For example, the command for selecting every field from a database
is this:

    SELECT * FROM Table;

  * The asterisk is a wildcard that represents **everything**.
  * It's like the asterisks used in the statement `from math import *`.

In this challenge, fill in the query in the **Code** tab to select everything
from the table `Employees`.

### Original Table

Name| Salary  
---|---  
Adam| 50000  
Bob| 30000  
Charlotte| 45000  
Dillon| 70000  
Eileen| 70000  
  
### Expected Results

Name| Salary  
---|---  
Adam| 50000  
Bob| 30000  
Charlotte| 45000  
Dillon| 70000  
Eileen| 70000  
  
### Notes

  * Write your statements inside `query = "your code here"`.
  * The convention is to generally use **capital letters** for SQL keywords, and to end every statement with a **semi-colon.**
  * Check out the **Resources** tab for more SQL tutorials and exercises.
  * See the rest of the challenges in this series [here!](https://edabit.com/collection/ZEmuGy8zxzDQdBb5o)

"""

query = "SELECT * FROM Employees;"

