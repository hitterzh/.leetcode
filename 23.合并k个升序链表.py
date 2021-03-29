#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode()
        index = head

        minval = float("inf")
        min = None
        minidx = 0

        while len(lists) != 0:

            flag = False
            for i, each in enumerate(lists):

                if each == None:
                    continue

                flag = True

                if each.val < minval:
                    minval = each.val
                    min = each
                    minidx = i
            if flag == False:
                break

            if min != None:
                index.next = min
                index = index.next

                lists[minidx] = min.next
                min = None
                minval = float('inf')

        return head.next


# @lc code=end

