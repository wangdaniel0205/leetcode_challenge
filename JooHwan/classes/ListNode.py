class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printAll(self):
        '''
        Print all nodes connected.
        '''
        cur, vals = self, []
        while cur:
            vals.append(str(cur.val))
            cur = cur.next
        print(' -> '.join(vals))

    @staticmethod
    def fromList(l):
        '''
        input: \n
            l: List\n
        output: \n
            head: ListNode (the first node of linked lists) \n
        Make nodes and connect them in order.
        '''
        if len(l) == 0:
            return None
        head = cur = ListNode(val=l[0])
        for val in l[1:]:
            cur.next = ListNode(val=val)
            cur = cur.next
        return head
