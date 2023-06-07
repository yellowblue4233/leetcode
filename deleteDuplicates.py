# 83. 删除排序链表中的重复元素
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list/
# 给定一个已排序的链表的头 head ，删除所有重复的元素，使每个元素只出现一次。返回 已排序的链表。

# 示例 1：
# 输入：head = [1,1,2]
# 输出：[1,2]

# 示例 2：
# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]

## 思路1：迭代方法
## 该题需要确保当前节点和下个节点不为空，判断当前节点的数值和下个节点的数值是否相同，
## 是则跳过下个节点，next指向下下个节点，否则不处理，轮到下个节点进行判断
## 注意：处理链表需要考虑空链表和单节点链表的特殊情况

from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            pass
        else:
            p = head
            while p.next is not None:
                if p.next.val == p.val:
                    p.next = p.next.next
                else:
                    p = p.next
        return head

## 思路2：递归方法
## 相当于倒序处理，从后面的最小链表开始处理
## 虽然递归方法代码简洁，但较难理解

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val else head
        ## 最后一句return相当于
        ## temp = head.next if head.val == head.next.val else head
        ## return temp
