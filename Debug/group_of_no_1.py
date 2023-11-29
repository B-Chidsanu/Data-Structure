
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