'''Given a singly linked list, determine if it is a palindrome.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        mNode = self.findMiddle(head)
        rNode = self.reverse(mNode)
        
        while rNode != None:
            if head.val != rNode.val:
                return False
            head = head.next
            rNode = rNode.next
        return True
    
    def findMiddle(self, node):
        slow = node
        fast = node
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self, node):
        prev = None
        cur = node
        while cur != None:
            tmp = cur
            cur = cur.next
            tmp.next = prev
            prev = tmp
        return prev