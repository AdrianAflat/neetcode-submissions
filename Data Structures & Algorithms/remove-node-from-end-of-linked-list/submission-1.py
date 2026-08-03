# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # [1,2,3,4]  n = 2
        # [1,2,4]

        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next

        removeIndex = N - n
        if removeIndex == 0:
            return head.next

        cur = head
        for i in range(N - 1):
            if (i + 1) == removeIndex:
                cur.next = cur.next.next
                break
            cur = cur.next

        return head
        
        # [1,2,3,4,5,6,7] n = 2
        #          1   2
        #       

        # [5] n = 1
        #  1
        #   2
    