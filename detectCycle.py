# 142. 环形链表 II
# https://leetcode.cn/problems/linked-list-cycle-ii/
# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 
# 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
# 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
# 不允许修改 链表。

# 示例 1：
# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。

# 示例 2：
# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。

# 示例 3：
# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

## 思路1：龟兔赛跑
## https://leetcode.cn/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode-solution/
## 快慢指针同时从head出发，慢指针移动一步，快指针移动两步，
## 当慢指针赶上快指针后，fast从头开始，每次移动一步，
## 最后快慢指针将会在入环节点相遇，返回此时的快指针或慢指针
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        else:
            slow = head.next
            fast = head.next.next
            while fast != slow:
                if fast is None or fast.next is None:
                    return None
                else:
                    slow = slow.next
                    fast = fast.next.next
            fast = head
            while fast != slow:
                slow = slow.next
                fast = fast.next
            return fast

## 思路2：Hashmap
## 和hasCycle函数大致一样，将返回值中的False换为None，True换为head
## 注意：在Python中，用于表示空值的常量是None，而不是NULL
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        else:
            hashmap = {}
            while head is not None:
                if hashmap.get(head):
                    return head
                else:
                    hashmap[head] = True
                    head = head.next
            return None