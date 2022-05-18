# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sumHead = currentSum = ListNode(None)
        n1 = l1
        n2 = l2
        rem = 0
        tempRem = 0
        
        while n1 or n2:
            if n1 is None:
                n1Val = 0
                n2Val = n2.val
            elif n2 is None:
                n2Val = 0
                n1Val = n1.val
            else:
                n2Val = n2.val
                n1Val = n1.val
                
            sumVal = n1Val + n2Val + rem
            if sumVal > 9:
                sumVal -= 10
                tempRem = 1
            else:
                tempRem = 0
            
            currentSum.next = ListNode(sumVal)
            currentSum = currentSum.next
            rem = tempRem
            
            n1 = n1.next if n1 else n1
            n2 = n2.next if n2 else n2
            
        if rem > 0:
            currentSum.next = ListNode(rem)
        
        result = sumHead.next
        sumHead.next = None
        
        return result
        