#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = ListNode(0, head)
        curr = prev
        next = head

        while next != None and n != 0:
            next = next.next
            n -= 1

        while next != None:
            next = next.next
            curr = curr.next

        curr.next = curr.next.next

        return prev.next


        

# @lc code=end

