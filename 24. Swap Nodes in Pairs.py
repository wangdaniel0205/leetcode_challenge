# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def swap(cur, prev=None):
            if not cur:
                return prev
            elif not prev:
                return swap(cur.next, cur)
            else:
                prev.next, cur.next = cur.next, prev
                prev.next = swap(prev.next)
                return cur
        
        return swap(head)