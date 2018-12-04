'''
Reverse a singly linked list.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None:
        return head
    last = ListNode(0)
    oldHead = head
    while head.next != None:
        head = head.next

    reverse(oldHead)
    oldHead.next = None

    return head

def reverse(node):
    if node.next != None:
        reverse(node.next)
        node.next.next = node
    return

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = None

reverseList(n1)