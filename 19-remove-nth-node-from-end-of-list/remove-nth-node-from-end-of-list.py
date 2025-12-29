# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1

        length = count - n
        if length == 0:
            return head.next

        curr = head
        for i in range(length - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        return head