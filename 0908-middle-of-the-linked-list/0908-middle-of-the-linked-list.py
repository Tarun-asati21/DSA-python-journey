# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # length of the ll
        count = 0
        curr = head
        while curr :
            count+=1
            curr = curr.next

        # search for the middle element
        k = count//2
        curr = head
        for i in range (k) :
            curr = curr.next
        head = curr
        return head
       
