# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        dummyHead = dummyCurrent = ListNode(None)
        h = []
        
        for ll in lists:
            if ll is None:
                continue
            heapq.heappush(h, [ll.val, ll])
            
        while h:
            val, ll = heapq.heappop(h)
            dummyCurrent.next = ll
            dummyCurrent = dummyCurrent.next
            if ll.next:
                ll = ll.next
                heapq.heappush(h, [ll.val, ll])
                
        return dummyHead.next
        
          