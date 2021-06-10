# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 and l2: 
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

from classes.ListNode import ListNode

if __name__ == '__main__':
    testCases = [
        [ListNode.fromList([1,2,4]), ListNode.fromList([1,3,4])],
        [ListNode.fromList([]),ListNode.fromList([])],
        [ListNode.fromList([]), ListNode.fromList([0])]
    ]

    solution = Solution()
    for case in testCases:
        ListNode.printAll(solution.mergeTwoLists(case[0], case[1]))
                
        