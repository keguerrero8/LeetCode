# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        mergedHead = mergedTail = ListNode(None)
        one = list1
        two = list2

        while one != None or two != None:
            oneVal = one.val if one != None else float("inf")
            twoVal = two.val if two != None else float("inf")
            if oneVal < twoVal:
                mergedTail.next = one
                one = one.next
            else:
                mergedTail.next = two
                two = two.next
            mergedTail = mergedTail.next

        return mergedHead.next
        