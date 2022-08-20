# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        total = []
        print(len(l1))
        if len(l1) >= len(l2):
            length = len(l2)
        else:
            length = len(l1)
        
        carry = 0
        for i in range(length):
            added = l1[i]+l2[i]+carry
            if added > 9:
                carry = added - 9
                total.append(added - 10)
            else:
                total.append(added)
                carry = 0
        
        return total
            
        
        