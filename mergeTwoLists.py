# 21. 合并两个有序链表
# https://leetcode.cn/problems/merge-two-sorted-lists/
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

# 示例 1：
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]

# 示例 2：
# 输入：l1 = [], l2 = []
# 输出：[]

# 示例 3：
# 输入：l1 = [], l2 = [0]
# 输出：[0]

## 思路1：迭代方法
## 为了可以在统一在循环中使用 p.next，先创建一个首节点answer，而answer.next就是要返回的结果节点，
## 不用answer而是用p来遍历，是为了保留answer和answer.next节点，不像list1和list2随着遍历而移动
## 注意：list1和list2代表链表的首节点，求链表长度需要遍历链表，编码时要考虑链表状态会如何改变

from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            answer = ListNode(0)
            p = answer
            while list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    p.next = list1
                    list1 = list1.next  
                else:
                    p.next = list2
                    list2 = list2.next
                p = p.next
            if list1 is not None:
                p.next = list1
            if list2 is not None:
                p.next = list2
            return answer.next

## 思路2：递归方法
## 比较并确定当前节点后，会留下两个新的链表，它们也可以继续用该函数进行合并，
## 每次递归就只确定一个节点，递归完成后就可以确定全部节点的顺序，
## 速度比迭代方法慢，递归所需的内存空间也比较大，但递归代码很简洁

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2