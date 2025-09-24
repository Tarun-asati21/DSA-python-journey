# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        hashmap={}
        while curr :
            if curr in hashmap:
                return curr
            hashmap[curr]=1
            curr=curr.next
        return None