"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        head, tail = self.flattenHelper(head)
        return head
    
    def flattenHelper(self, head):
        prev = None
        current = head
        while current:
            if current.child:
                flathead, flattail = self.flattenHelper(current.child)
                temp = current.next
                current.next = flathead
                flathead.prev = current
                flattail.next = temp
                if temp:
                    temp.prev = flattail
                prev = flattail
                current.child = None
                current = temp
            else:
                prev = current
                current = current.next
        
        
        return head, prev
        