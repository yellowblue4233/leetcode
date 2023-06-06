## Python 快速排序法，时间复杂度O(nlogn)
def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    return list

def partition(list, start, end):
    i = start - 1
    for j in range(start, end):
        if list[j] < list[end]:
            i = i + 1
            swap(list, i, j)
    i = i + 1
    swap(list, i, end)
    return i

def quicksort(list, start, end):
    if start < end:
        middle = partition(list, start, end)
        quicksort(list, start, middle - 1)
        quicksort(list, middle + 1, end)
    return list

def sort_idx(sort, list):
    assert len(sort) == len(list), "sort_idex:len(sort) != len(list)"
    idx = [-1 for _ in range(len(sort))]
    for i_idx, i_val in enumerate(sort):
        for j_idx, j_val in enumerate(list):
            if i_val == j_val and (j_idx not in idx):     # 需考虑值相同的情况
                idx[i_idx] = j_idx
    return idx


if __name__ == '__main__':
    a = [1,5,8,9,0,3,2,4,6,7]
    quicksort(a, 0, len(a) - 1)
    print(a)