# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
slow and fast pointer to come up with midpoint
take slow pointer iterate through and reverse the pointers




'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse linked list
        curr = slow.next
        slow.next = None
        prev = slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        #merge alternating linked lists
        #heads are head, prev
        second = prev
        first = head

        while second:
            temp1 = first.next
            first.next = second
            temp2 = second.next
            second.next = temp1
            first = temp1
            second = temp2






        


            

        
        

        
        

        
        
