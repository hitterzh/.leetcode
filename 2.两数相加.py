#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 == None and l2 == None:
            return None
        
        res = None
        carrybit = 0
        current = None

        while l1 != None and l2 != None:
            
            node = ListNode(0)

            sum = l1.val + l2.val + carrybit
            node.val = sum % 10
            carrybit = sum // 10

            l1 = l1.next
            l2 = l2.next

            if res:
                current.next = node
                current = current.next
            else:
                res = node
                current = res

        while l1 != None:
            node = ListNode(0)

            sum = l1.val + carrybit
            node.val = sum % 10
            carrybit = sum // 10

            l1 = l1.next

            if res:
                current.next = node
                current = current.next
            else:
                res = node
                current = res

        while l2 != None:
            node = ListNode(0)

            sum = l2.val + carrybit
            node.val = sum % 10
            carrybit = sum // 10

            l2 = l2.next

            if res:
                current.next = node
                current = current.next
            else:
                res = node
                current = res

        if carrybit:
            node = ListNode(0)
            node.val = carrybit
            current.next = node


        return res





            

# @lc code=end

