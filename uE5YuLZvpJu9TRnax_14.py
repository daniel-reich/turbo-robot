"""


Create a function that takes a mathematical expression in **prefix notation**
as a string and evaluates the expression.

### Examples

    prefix("+ 5 4") ➞  9
    
    prefix("* 12 2") ➞  24
    
    prefix("+ -10 10") ➞  0

### Notes

  * The mathematical expression is valid.
  * Check the **Resources**.
  * Use `//` for division.

"""

def prefix(exp):
    exp_lst = exp.split()
    cnt = 0
    for item in exp_lst:
        if item in "+-*/":
            cnt += 1
    if cnt == 1:
        if exp_lst[0] == "+":
            if exp_lst[1][0] != "-" and exp_lst[2][0] != "-":
                return int(exp_lst[1]) + int(exp_lst[2])
            elif exp_lst[1][0] == "-" and exp_lst[2][0] != "-":
                return -1 * int(exp_lst[1][1:]) + int(exp_lst[2])
            elif exp_lst[1][0] != "-" and exp_lst[2][0] == "-":
                return int(exp_lst[1]) + (int(exp_lst[2][1:]) * -1)
            else:
                return (int(exp_lst[1][1:])*-1) + (int(exp_lst[2][1:]) * -1)
        if exp_lst[0] == "-":
            if exp_lst[1][0] != "-" and exp_lst[2][0] != "-":
                return int(exp_lst[1]) - int(exp_lst[2])
            elif exp_lst[1][0] == "-" and exp_lst[2][0] != "-":
                return (-1 * int(exp_lst[1][1:])) - int(exp_lst[2])
            elif exp_lst[1][0] != "-" and exp_lst[2][0] == "-":
                return int(exp_lst[1]) - (int(exp_lst[2][1:]) * -1)
            else:
                return (-1 * int(exp_lst[1][1:])) - (-1 * int(exp_lst[2][1:]))
        if exp_lst[0] == "*":
           if exp_lst[1][0] != "-" and exp_lst[2][0] != "-":
               return int(exp_lst[1]) * int(exp_lst[2])
           elif exp_lst[1][0] == "-" and exp_lst[2][0] != "-":
               return -1 * int(exp_lst[1][1:]) * int(exp_lst[2])
           elif exp_lst[1][0] != "-" and exp_lst[2][0] == "-":
                return int(exp_lst[1]) * int(exp_lst[2][1:]) * -1
           else:
                return int(exp_lst[1][1:]) * int(exp_lst[2][1:])
        if exp_lst[0] == "/":
            if exp_lst[1][0] != "-" and exp_lst[2][0] != "-":
               return int(exp_lst[1]) // int(exp_lst[2])
            elif exp_lst[1][0] == "-" and exp_lst[2][0] != "-":
               return (-1 * int(exp_lst[1][1:])) // int(exp_lst[2])
            elif exp_lst[1][0] != "-" and exp_lst[2][0] == "-":
               return int(exp_lst[1]) // (int(exp_lst[2][1:]) * -1)
            else:
                return (-1 *int(exp_lst[1][1:])) // (-1 * int(exp_lst[2][1:]))
​
    elif cnt > 1:
        for i in range(len(exp_lst)-1, -1, -1):
            if exp_lst[i] in "+-*/":
                break
        if i < cnt:
              first_result = prefix(exp_lst[cnt-1] + ' ' + exp_lst[cnt] + ' ' + exp_lst[cnt+1])
              remain_to_calculate = ' '.join(exp_lst[:cnt-1] + [str(first_result)] + exp_lst[cnt+2:])
              return prefix(remain_to_calculate)
        else:
            first_result = prefix(exp_lst[i] + ' ' + exp_lst[i + 1] + ' ' + exp_lst[i + 2])
            remain_to_calculate = ' '.join(exp_lst[:i] + [str(first_result)] + exp_lst[i + 3:])
            return prefix(remain_to_calculate)

