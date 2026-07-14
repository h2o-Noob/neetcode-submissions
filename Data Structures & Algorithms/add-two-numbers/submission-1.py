# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = l1
        curr2 = l2
        num1,num2,summ = 0,0,0
        multi = 1

        while curr1:
            num1 += curr1.val * multi
            curr1 = curr1.next
            multi *= 10
        
        multi = 1

        while curr2:
            num2 += curr2.val * multi
            curr2 = curr2.next
            multi *= 10
        
        summ = num1 + num2


        dummy = ListNode()
        current = dummy

        if summ == 0:
            return ListNode(0)

        while summ >= 1:
            new_node = ListNode(summ%10)
            current.next = new_node
            current = current.next
            summ = summ//10
        
        head = dummy.next

        return head
            

        
            

        

        

            
        