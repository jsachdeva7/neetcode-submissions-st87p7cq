# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        summation = ListNode(-1)
        current1 = l1
        current2 = l2
        carryOver = 0
        currentOnSum = summation
        while current1 or current2 or carryOver > 0:
            # if digit exists, it's the digit, else 0
            dig1 = current1.val if current1 else 0
            dig2 = current2.val if current2 else 0

            # calculate sum and carryover
            digSum = dig1 + dig2 + carryOver
            if digSum >= 10:
                carryOver = 1
                digit = digSum - 10
            else:
                carryOver = 0
                digit = digSum
            
            # digit for new node in sum list
            currentOnSum.next = ListNode(digit)

            # advance on list 1 and 2 and sum list
            if current1:
                current1 = current1.next
            if current2:
                current2 = current2.next
            currentOnSum = currentOnSum.next
        
        return summation.next
            
        