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