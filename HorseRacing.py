## Python 田忌赛马/优势洗牌
from QuickSort import quicksort, sort_idx

def horse_racing(list_A, list_B):
    assert len(list_A) == len(list_B), "horse_racinglen(list_A) != len(list_B)"
    ## 为A和B排序，并获得B中排序后的值对应的排序前的索引
    list_len = len(list_A)
    sort_A = quicksort(list_A.copy(), 0, list_len - 1)
    sort_B = quicksort(list_B.copy(), 0, list_len - 1)
    idx_B = sort_idx(sort_B, list_B)
    
    ans_A = [-1 for _ in range(list_len)]
    flag_win = 0    # 胜利标志，正数A胜，负数A负，0为平局
    
    j = 0         # j为sort_B的指针，慢指针
    dis_A = []    # 存放A中无用的值
    for i in range(list_len):     # i为sort_A的指针，快指针
        if sort_A[i] > sort_B[j]:
            ans_A[idx_B[j]] = sort_A[i]
            flag_win = flag_win + 1
            j = j + 1
        else:
            dis_A.append(sort_A[i])
    for k in range(j, list_len):  # 慢指针j的后续处理
        ans_A[idx_B[k]] = dis_A.pop()
        flag_win = flag_win - 1
    return ans_A, flag_win


if __name__ == '__main__':
    A = [19, 14, 17, 13, 11, 9]
    B = [10, 16, 20, 12, 21, 16]
    print("A: {0}".format(A))
    print("B: {0}".format(B))
    
    ans_A, flag_win = horse_racing(A, B)
    print("----------------------------------------------------------")
    
    if flag_win > 0:
        print("胜, 新的排列顺序为{0}".format(ans_A))
    elif flag_win < 0:
        print("负, 新的排列顺序为{0}".format(ans_A))
    else:
        print("平, 新的排列顺序为{0}".format(ans_A))
    
