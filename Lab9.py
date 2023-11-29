# ข้อ1
def isPalindrome(str):
    if len(str) <= 1:  # base case
        return True
    elif str[0] != str[-1]:  # base case
        return False
    else:  # recursive cases
        return isPalindrome(str[1:-1])


checklist = ["abcdcba", "atoyota", "kmitl",
             "manassanan", "programming", "fundamental"]
for i in checklist:
    print(isPalindrome(i))


# ข้อ2
def isAscending(list_of_integer):
    if len(list_of_integer) < 1:  # base case
        return True
    elif list_of_integer[0] <= list_of_integer[-1]:  # recursive cases
        return isAscending(list_of_integer[1:-1])
    else:  # base case
        return False


checklist = [[1, 2, 3, 4, 5, 6, 7], [3, 4, 2, 5, 6, 1, 2], [9, 8, 7, 6, 5, 4], [
    0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5], [6, 7, 8, 9, 10, 11, 12], [6, 3, 8, 7, 9, 2, 3, 1, 5]]

for i in checklist:
    print(isAscending(i))


# ข้อ3
def group_of_no_1(island_list, point_no):
    if point_no >= len(island_list) or point_no <= 0:  # base case
        return 0
    if island_list[point_no] == 0 or island_list[point_no] == 2:  # base case
        return 0
    if island_list[point_no] == 1:  # recursive cases
        island_list[point_no] = 2
        return 1 + group_of_no_1(island_list, point_no-1) + group_of_no_1(island_list, point_no+1)


print(group_of_no_1([1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0], 1))
print(group_of_no_1([1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0], 5))
print(group_of_no_1([1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], 4))
print(group_of_no_1([1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], 10))
print(group_of_no_1([1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], 1))
print(group_of_no_1([0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 7))


# ข้อ4
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


for ckeck in ["(()()(())())", "((()()", "())()()(", "(((()))((())))", "()()(((())))", "()"]:
    print("str =", ckeck, "=", valid_parentheses(ckeck))
