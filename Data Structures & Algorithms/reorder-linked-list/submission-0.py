# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        c1 = head
        c2 = head

        while c2 and c2.next:
            c1 = c1.next
            c2 = c2.next.next
        
        c2 = c1.next
        c1.next = None

        prev = None

        while c2:
            nxt = c2.next
            c2.next = prev
            prev = c2
            c2 = nxt
        
        c1 = head
        c2 = prev

        while c2:
            nxt1 = c1.next
            nxt2 = c2.next

            c1.next = c2
            c2.next = nxt1

            c1 = nxt1
            c2 = nxt2


            
            


        

        


        


        