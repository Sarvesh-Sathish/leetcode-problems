from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(self, head: Optional[ListNode]) -> bool:
    if head == None:
        return False
    curr = head
    visitedNodes = []
    while curr.next != None:
        if curr in visitedNodes:
            return True
        else:
            visitedNodes.append(curr)
            curr = curr.next
    return False