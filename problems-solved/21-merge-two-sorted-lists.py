from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return list1
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        retNode = ListNode()
        if list1.val < list2.val:
            retNode.val = list1.val
            list1 = list1.next
        else:
            retNode.val = list2.val
            list2 = list2.next
        currNode = retNode
        while list1 is not None and list2 is not None:
            currNode.next = ListNode()
            currNode = currNode.next
            if list1.val < list2.val:
                currNode.val = list1.val
                list1 = list1.next
            else:
                currNode.val = list2.val
                list2 = list2.next
        while list1 is not None:
            currNode.next = ListNode()
            currNode = currNode.next
            currNode.val = list1.val
            list1 = list1.next
        while list2 is not None:
            currNode.next = ListNode()
            currNode = currNode.next
            currNode.val = list2.val
            list2 = list2.next
        return retNode

        
        l