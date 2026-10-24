# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        l = 0
        #get length of list
        dummy = head
        while dummy:
            l += 1
            dummy = dummy.next
        if l == n and l == 1:
            return None
        if l == n:
            return head.next
        #get mth node from start of list
        m = l - n

        curr = head
        for _ in range(1, m): #repeat m times
            curr = curr.next
        
        node = curr.next.next
        curr.next = node
        return head

        
