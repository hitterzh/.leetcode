#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        idx = head
        cnt = 0

        while idx != None :
            cnt += 1
            idx = idx.next

        if cnt < k:
            return head

        prev = head
        cur = head.next
        cnt = k
        nxt = None

        while prev != None and cur != None and cnt > 1:
            nxt = cur.next

            cur.next = prev

            prev = cur
            cur = nxt
            cnt -= 1

        head.next = self.reverseKGroup(cur, k)
        return prev
        

        




# @lc code=end

