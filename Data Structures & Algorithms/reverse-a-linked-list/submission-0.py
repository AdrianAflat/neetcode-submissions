# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 -> 1 -> 2 -> 3 ->
        # 3 -> 2 -> 1 -> 0 ->

        prev = None
        curr = head 

        while curr: 
            nextVal = curr.next
            curr.next = prev
            prev = curr
            curr = nextVal

        return prev

    # 0 -> 1 -> 2 -> 3 ->
    # prev = 0
    # curr = 1

    # nextVal = 2
    # curr.next = 0
    # prev = 1