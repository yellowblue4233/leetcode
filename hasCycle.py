# 141. 环形链表
# https://leetcode.cn/problems/linked-list-cycle/
# 给你一个链表的头节点 head ，判断链表中是否有环。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
# 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。

# 示例 1：
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。

# 示例 2：
# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。

# 示例 3：
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

## 思路1：龟兔赛跑（官方代码）
## 用快慢指针来遍历链表，慢指针移动一步，快指针移动两步，
## 如果链表有环，则慢指针一定能赶上快指针
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next    
        return True

## 思路2：Hashmap
## 将遍历过的节点（主要节点地址或其他唯一识别符）存入Hashmap中，
## 如果当前节点存在于Hashmap中，则链表有环
## 注意：在Python中，通常无法直接获取对象的内存地址。Python提供了内置函数id()，
## 可以用于获取对象的唯一标识符，但它并不表示对象在内存中的确切地址。
## 这里将节点直接存入字典，Leetcode官方没有使用字典而是使用set()直接保存节点

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:    
        if head is None or head.next is None:
            return False
        else:
            hashmap = {}
            while head is not None:
                if hashmap.get(head):
                    return True
                else:
                    hashmap[head] = True
                    head = head.next
            return False