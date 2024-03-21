from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        firstIter = l1
        secondIter = l2

        carry = 0
        sum = ListNode()
        retNode = sum
        prev = None
        while firstIter is not None and secondIter is not None:
            innerSum = firstIter.val + secondIter.val + carry
            sum.val = innerSum % 10
            print(sum.val)
            sum.next = ListNode()
            prev = sum
            sum = sum.next
            carry = int(innerSum / 10)
            firstIter = firstIter.next
            secondIter = secondIter.next
            
        
        while firstIter is not None:
            innerSum = firstIter.val + carry
            sum.val = innerSum % 10
            print(sum.val)
            sum.next = ListNode()
            prev = sum
            sum = sum.next
            carry = int(innerSum / 10)
            firstIter = firstIter.next
            
        while secondIter is not None:
            innerSum = secondIter.val + carry
            sum.val = innerSum % 10
            print(sum.val)
            sum.next = ListNode()
            prev = sum
            sum = sum.next
            carry = int(innerSum / 10)
            secondIter = secondIter.next
        
        if carry:
            sum.val = carry
        else:
            prev.next = None

        return retNode