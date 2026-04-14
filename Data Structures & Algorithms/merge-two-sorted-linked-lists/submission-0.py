# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode(-1)
        currentNode1 = list1
        currentNode2 = list2
        currentNode3 = list3
        while currentNode1 and currentNode2:
            if currentNode1.val <= currentNode2.val:
                currentNode3.next = currentNode1
                currentNode1 = currentNode1.next
            else:
                currentNode3.next = currentNode2
                currentNode2 = currentNode2.next
            currentNode3 = currentNode3.next
        if not currentNode1:
            currentNode3.next = currentNode2
        else:
            currentNode3.next = currentNode1
        
        return list3.next

