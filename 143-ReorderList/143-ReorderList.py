# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return

        slow = head
        stack = []
        
        while slow:
            stack.append(slow)
            slow = slow.next
        
        current = head
[1,2,3,4]
