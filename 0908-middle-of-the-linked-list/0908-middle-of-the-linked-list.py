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
        count = 0
        curr = head
        while curr :
            count+=1
            curr = curr.next
        
        # if count%2 != 0 :
        k = count//2
        curr = head
        for i in range (k) :
            curr = curr.next
        head = curr
        return head
        # else :
        #     k= count//2
        #     curr = head
        #     for i in range (k) :
        #         curr = curr.next
        #     head = curr
        #     return head

