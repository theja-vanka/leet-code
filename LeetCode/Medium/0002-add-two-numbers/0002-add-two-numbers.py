# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        l0 = ListNode(0)
        rl = l0
        while l1 and l2:
            _ = l1.val + l2.val + carry
            l0.next = ListNode(_  % 10)
            carry = _ // 10
            l1 = l1.next
            l2 = l2.next
            l0 = l0.next
        
        while l1:
            _ = l1.val +  carry
            l0.next = ListNode(_  % 10)
            carry = _ // 10
            l1 = l1.next
            l0 = l0.next
        
        while l2:
            _ = l2.val +  carry
            l0.next = ListNode(_  % 10)
            carry = _ // 10
            l2 = l2.next
            l0 = l0.next

        if carry:
            l0.next = ListNode(carry)
            l0 = l0.next

        return rl.next