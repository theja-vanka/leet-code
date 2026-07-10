# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy: Optional[ListNode] = ListNode()
        result: Optional[ListNode] = dummy
        carry: int = 0
        while l1 and l2:
            _ = l1.val + l2.val + carry
            dummy.next = ListNode(_%10)
            carry = _ // 10
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            _ = l1.val + carry
            dummy.next = ListNode(_%10)
            carry = _ // 10
            dummy = dummy.next
            l1 = l1.next
        
        while l2:
            _ = l2.val + carry
            dummy.next = ListNode(_%10)
            carry = _ // 10
            dummy = dummy.next
            l2 = l2.next
        
        if carry:
            dummy.next = ListNode(carry)

        return result.next
        