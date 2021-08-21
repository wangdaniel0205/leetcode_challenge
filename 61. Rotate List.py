# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return 
        length = 1
        end = head
        while end.next:
            length += 1
            end = end.next
            
        k = k % length
        cur = head
        for _ in range(length - k - 1):
            cur = cur.next
        
        end.next = head
        res = cur.next
        cur.next = None
        return res
        
        
        
        