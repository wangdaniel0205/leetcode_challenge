'''
if __name__ == '__main__':
    testCases = [
        [ListNode.fromList([1,2,4]), ListNode.fromList([1,3,4])],
        [ListNode.fromList([]),ListNode.fromList([])],
        [ListNode.fromList([]), ListNode.fromList([0])]
    ]

    solution = Solution()
    for case in testCases:
        ListNode.printAll(solution.mergeTwoLists(case[0], case[1]))
'''