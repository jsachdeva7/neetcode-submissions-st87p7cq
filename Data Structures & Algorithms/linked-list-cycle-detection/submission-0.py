# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visitedNodes = set()
        currentNode = head
        while currentNode:
            if currentNode in visitedNodes:
                return True
            else:
                visitedNodes.add(currentNode)
            currentNode = currentNode.next
        return False