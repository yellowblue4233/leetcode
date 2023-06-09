# 206. 反转链表
# https://leetcode.cn/problems/reverse-linked-list/
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

# 示例 1：
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]

# 示例 2：
# 输入：head = [1,2]
# 输出：[2,1]

# 示例 3：
# 输入：head = []
# 输出：[]

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## 思路1：迭代方法
## 因为用next遍历链表不会后退，所以参与反转操作的上个节点需要保存，
## 因为将当前节点的next改为上个节点会导致链表断裂，需要先保存下个节点再反转，
## 最后，先将当前节点变为上个节点，再将当前节点变为事先保存的下个节点
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        while head:
            temp = head.next    ## 保存下个节点temp
            head.next = prev    ## 当前节点head的反转操作
            prev = head    ## 将当前节点head变为上个节点prev
            head = temp    ## 将下个节点temp变为当前节点head
        return prev

## 思路2：递归方法
## https://leetcode.cn/problems/reverse-linked-list/solution/fan-zhuan-lian-biao-by-leetcode-solution-d1k2/
## （递归方法是真难想）递归方法从后面开始执行，先从简单的例子开始考虑，扩展到复杂的例子：
## 例如示例[1,2,3,4,5]，该递归方法的函数self.reverseList的输入依次为[1,2,3,4,5]，[2,3,4,5]，[3,4,5]，[4,5]，[5]，
## 1）先是执行输入为[5]的函数，触发if not head.next，直接返回[5]，该返回值参与下一个函数执行，
## 2）然后执行输入为[4,5]的函数，ptr = self.reverseList([5]) = [5]，之后反转链表为None<-[4]<-[5]，最后返回[5]
## 3）接着执行输入为[3,4,5]的函数，此时，链表为[3]->[4]<-[5]，这里节点[3]是指向[4]的，这点没有因为之前的操作改变，
##    ptr = self.reverseList([4,5]) = self.reverseList([5]) = [5]，可见，ptr一直都会是[5]，
##    所以递归方法的最终返回值是节点[5]，就是这样将递归方法的返回值保持为链表反转后的首节点[5]，
##    之后反转链表为None<-[3]<-[4]<-[5]，最后返回[5], ......
## 以此类推，直到反转整个列表，None<-[1]<-[2]<-[3]<-[4]<-[5]，返回节点[5]
## 注意：在链表的递归方法中，用来实现递归的self.函数(head.next)的返回值不是必须为head.next
## 即是不返回head.next，链表的状态还是被改变了，所以在这里返回值被用来保持反转列表的首节点了
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        ptr = self.reverseList(head.next)    ## 用来返回反转链表的首节点
        (head.next).next = head    ## 真正的链表反转操作，修改下个节点的next指向
        head.next = None    ## 确保反转后的链表最后节点为None，即保证链表无环
        return ptr