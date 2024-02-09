# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        temp = res
        arr = []

        for i in lists:
            buck = i
            while buck:
                heapq.heappush(arr, buck.val)
                buck = buck.next
        
        while arr:
            temp.next = ListNode(heapq.heappop(arr))
            temp = temp.next
[[1,4,5],[1,3,4],[2,6]]
