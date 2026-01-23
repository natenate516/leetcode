# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr and curr.next:
            nxt = curr.next

            curr.next = nxt.next
            nxt.next = curr
            prev.next = nxt

            prev = curr
            curr = curr.next

        return dummy.next
