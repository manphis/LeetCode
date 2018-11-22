"""
Remove all elements from a linked list of integers that have value val.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    if head == None:
        return head

    node = ListNode(0)
    prev = node
    prev.next = head

    while head != None:
        if head.val == val:
            prev.next = head.next;
            head = head.next;
        else:
            prev = head;
            head = head.next;
    return node.next


# test
a = ListNode(6)
b = ListNode(1)
c = ListNode(2)
a.next = b
b.next = c

result = removeElements(a, 6)

print(result)