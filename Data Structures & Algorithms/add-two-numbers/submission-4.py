# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        
        curr1, curr2 = l1, l2
        num1 = num2 = 0
        multi = 1

        while curr1:
            num1 += curr1.val * multi
            multi *= 10
            curr1 = curr1.next

        multi = 1
        while curr2:
            num2 += curr2.val * multi
            multi *= 10
            curr2 = curr2.next

        summ = num1 + num2

        dummy = ListNode()
        current = dummy

        # handle case where sum is 0
        if summ == 0:
            return ListNode(0)

        while summ > 0:
            current.next = ListNode(summ % 10)
            current = current.next
            summ //= 10   # ✅ FIX

        return dummy.next





            

        
            

        

        

            
        