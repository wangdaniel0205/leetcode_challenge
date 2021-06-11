# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from classes.ListNode import ListNode
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        resHead = ListNode()
        resCur = resHead
        carry = False
        while l1 != None or l2 != None:
            
        
            if l1 == None:
                node, carry = self.addNode(0, l2.val, carry=carry)
                l2 = l2.next
                
            elif l2 == None:
                node, carry = self.addNode(l1.val, 0, carry=carry)
                l1 = l1.next
                
            else:
                node, carry = self.addNode(l1.val, l2.val, carry=carry)
                l1 = l1.next
                l2 = l2.next
                
            resCur.next = node
            resCur = resCur.next
        
        
        if carry:
            resCur.next = ListNode(val = 1)
        return resHead.next
    
    
    
    def addNode(self, val1, val2, carry=False):
        res = val1 + val2
        if carry:
            res += 1
        carryFlag = False
        if res >= 10:
            res -= 10
            carryFlag = True
        return ListNode(val = res), carryFlag