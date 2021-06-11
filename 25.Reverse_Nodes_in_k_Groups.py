# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(head, k):
            cur, nxt = head, head.next
            for i in range(k-1):
                prev, cur, nxt = cur, nxt, nxt.next
                cur.next = prev
            head.next = nxt
            return cur, head
            

        cur, listLen = head, 0
        while cur:
            listLen+=1
            cur = cur.next
        
        kLoop = listLen//k
        
        if kLoop > 0:
            head, cur = reverse(head, k)
            for i in range(kLoop-1):
                cur.next, cur = reverse(cur.next, k)
        
        return head