# ข้อที่ 1
import math
import random
import time
st = time.time()


def remove_even(lst):
    # insert code here
    return [num for num in lst if num % 2 != 0]


A = [1, 2, 3, 4, 5, 6, 7]
B = remove_even(A)
print(B)  # [1,3,5,7]
time.sleep(1)
en = time.time()
elapsed_time = en - st

print('Execution time:', elapsed_time, 'seconds')

st = time.time()


def remove_even(lst):
    # insert code here
    return {num for num in lst if num % 2 != 0}


A = {1, 2, 3, 4, 5, 6, 7}
B = remove_even(A)
print(B)  # [1,3,5,7]
time.sleep(1)
en = time.time()
elapsed_time = en - st

print('Execution time:', elapsed_time, 'seconds')


# ข้อที่ 3.1
rnddat = [random.randint(1, 1000) for i in range(0, 100)]
OrderedList = ['' for i in range(len(rnddat))]


def QuickSort(lists, OrderedLists, index):
    if len(lists) == 0:
        return OrderedLists
    UList = []
    LList = []
    pivot = random.choice(lists)
    lists.remove(pivot)
    for i in lists:
        if i > pivot:
            UList.append(i)
        else:
            LList.append(i)
    OrderedLists[index+len(LList)] = pivot
    QuickSort(UList, OrderedLists, index+len(LList)+1)
    QuickSort(LList, OrderedLists, index)
    return OrderedLists


ans = QuickSort(rnddat, OrderedList, 0)
print(ans)


# ข้อที่ 3.2
Ent_input = int(input("Enter Input :"))
dat = list(range(1, 1000001))
half = dat[-1]/2
split_index = half

while split_index != 1:
    l_arr = dat[:int(split_index)]
    r_arr = dat[int(split_index):]
    if Ent_input in l_arr:
        dat = l_arr
    else:
        dat = r_arr
    found = dat[0] if Ent_input == dat[0] else dat[1] if Ent_input == dat[1] else 0
    if found != 0:
        print(f"found ! :{found}")
        break
    split_index = math.ceil(split_index / 2)
