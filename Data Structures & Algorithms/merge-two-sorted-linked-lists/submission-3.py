# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: #if both empty
            return None
        if not list1: #if list 1 is empty
            return list2
        if not list2:
            return list1

        list3 = None

        curr1 = list1
        curr2 = list2

        while curr1 or curr2: #while both lists have elements
            if curr1 == None:
                v1 = 101
            else:
                v1 = curr1.val
            if curr2 == None:
                v2 = 101
            else:
                v2 = curr2.val
            
            if v1 <= v2: #insert v1
                if list3: #if list3 already has element
                    curr3.next = ListNode(v1)
                    curr3 = curr3.next
                else: 
                    list3 = ListNode(v1)
                    curr3 = list3

                curr1 = curr1.next

            else: #v1 > v2
                if list3: #if list3 already has element
                    curr3.next = ListNode(v2)
                    curr3 = curr3.next
                else: 
                    list3 = ListNode(v2)
                    curr3 = list3
                curr2 = curr2.next
        
        return list3




