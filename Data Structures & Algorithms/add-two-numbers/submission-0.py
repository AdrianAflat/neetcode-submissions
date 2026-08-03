# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = 0
        cur1 = l1
        mult = 1
        while cur1:
            num1 += (cur1.val * mult)
            mult *= 10
            cur1 = cur1.next
        
        num2 = 0
        cur2 = l2
        mult = 1
        while cur2:
            num2 += (cur2.val * mult)
            mult *= 10
            cur2 = cur2.next

        resultSum = num1 + num2

        dummy = ListNode()
        cur = dummy
        for num in reversed(str(resultSum)):
            cur.next = ListNode(int(num))
            cur = cur.next

        return dummy.next
        
       
        
        
        