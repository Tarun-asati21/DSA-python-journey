# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # iterative approach 
        temp= head
        prev= None
        while temp :
            front = temp.next # temporay store kar rahe hai, aage waala node
            temp.next = prev # current node, picche waale node ko point kare 
            prev = temp # picche waala node, aage bhadao 
            temp = front # current node aage bhadao
        return prev
