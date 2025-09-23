# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # tc = O(n)
        # delete karne waale node me, aage waale node ki value daal do
        node.val = node.next.val 

        # delete karne waala node aage waale ko point kar raha tha, tum uske aage ke aage waale ko point kar do 
        node.next = node.next.next 