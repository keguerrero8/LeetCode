"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None
        oldToNewMap = {}
        cur = head
        newHead = newCurrent = Node(0)
        
        while cur:
            if cur not in oldToNewMap:
                oldToNewMap[cur] = Node(cur.val)
                
            newCurrent.next = oldToNewMap[cur]
            newCurrent = newCurrent.next
            
            if cur.random not in oldToNewMap:
                oldToNewMap[cur.random] = Node(cur.random.val) if cur.random else None
                
            newCurrent.random = oldToNewMap[cur.random]
            cur = cur.next
            
        newCurrent.next = None
        return newHead.next