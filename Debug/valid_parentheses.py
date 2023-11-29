def valid_parentheses(str, i=0, cnt=0):
    if i == len(str):  # base case
        return cnt == 0
    if cnt < 0:  # base case
        return False
    if str[i] == "(":  # recursive cases
        return valid_parentheses(str, i + 1, cnt + 1)
    elif str[i] == ")":  # recursive cases
        return valid_parentheses(str, i + 1, cnt - 1)
    return valid_parentheses(str, i + 1, cnt)


for ckeck in [ "())"]:
    print("str =", ckeck, "=", valid_parentheses(ckeck))