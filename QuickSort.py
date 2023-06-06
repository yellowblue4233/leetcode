## Python 快速排序法，时间复杂度O(nlogn)
## 思路：1.选择与最后一个数作比较，将较小的数交换到前面，较大的数留到后面，
## 而最后的数最终会排在准确的位置上，之后以该位置作分界线将列表从中间分为较小和较大的两段，
## 重复之前的位置交换，迭代运行，直到所有的数排列完毕。
def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    return list

def partition(list, start, end):
    i = start - 1    # 慢指针，指出较小的数的存放位置
    for j in range(start, end):    # 快指针，遍历列表
        if list[j] < list[end]:    # 如果快指针所指的数比最后的数的小，则交换位置
            i = i + 1    # 每交换一次，慢指针前进一步
            swap(list, i, j)
    i = i + 1    # 因为循环到最后list[j]与list[end]相等，所以最后一次循环的i+1不执行
    swap(list, i, end)    # 将最后的数交换到准确的位置，前面的数比它小，后面的数比它大
    return i    # 此时位置i为较小的数与较大的数的分界线

def quicksort(list, start, end):
    if start < end:    # 当列表为空或长度为1时，没必要排序
        middle = partition(list, start, end)    # 排列后从中间分为两段
        quicksort(list, start, middle - 1)    # 较小的一段进行排列
        quicksort(list, middle + 1, end)    # 较大的一段进行排列
    return list

def sort_idx(sort, list):
    "返回排列前的列表索引"
    assert len(sort) == len(list), "sort_idex:len(sort) != len(list)"
    idx = [-1 for _ in range(len(sort))]
    for i_idx, i_val in enumerate(sort):
        for j_idx, j_val in enumerate(list):
            if i_val == j_val and (j_idx not in idx):    # 需考虑值相同的情况
                idx[i_idx] = j_idx
    return idx


if __name__ == '__main__':
    a = [1,5,8,9,0,3,2,4,6,7]
    quicksort(a, 0, len(a) - 1)
    print(a)