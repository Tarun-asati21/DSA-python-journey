# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def gcd(a,b):
            while b :
                a,b = b,a%b
            return a 
        
        curr = head
        while curr.next :
            temp = curr.next
            a=curr.val
            b=temp.val
            insert_val = gcd(a,b)
            insert_node = ListNode(insert_val)
            curr.next = insert_node
            insert_node.next = temp
            curr = temp
        return head
        