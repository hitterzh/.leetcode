#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def recurSwap(n: ListNode) -> ListNode:
            if n == None or n.next == None:
                return n

            cur = n
            nxt = cur.next

            cur.next = recurSwap(nxt.next)
            nxt.next = cur

            return nxt

        return recurSwap(head)

            


        





'''
    def swapPairs(self, head: ListNode) -> ListNode:

        first = head

        prev = ListNode(0, head)
        res = prev

        while first != None and first.next != None:
            second = first.next

            first.next = second.next
            second.next = first
            prev.next = second
            
            prev = first
            first = first.next

        return res.next
'''




            

# @lc code=end

