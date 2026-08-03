# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, 1, 2, 3, 4, 5, 6]
        # [0, 6, 1, 5, 2, 4, 3]
        #           s        f

        # find the middle and the end
        fast = head
        slow = head 
        while fast and fast.next:
            fast = fast.next.next # end of the list 
            slow = slow.next      # middle point

        secondStart = slow.next
        slow.next = None

        # reverse the second half of the nodes
        curr = secondStart
        prev = None
        while curr:
            nextNode = curr.next 
            curr.next = prev
            prev = curr
            curr = nextNode

        # build the output 
        first = head  # start of first list
        second = prev # start of second list
        while second:
            next1 = first.next
            next2 = second.next

            first.next = second
            second.next = next1
            first = next1
            second = next2


            



            
        
        