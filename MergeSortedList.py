"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #return l2 if l1 is empty
        if not l1:
            return l2
        
        #return l1 if l2 is empty
        if not l2:
            return l1   
        
        #create a dummy node
        dummy = ListNode(-1)
        cur = dummy
        
        #iterate over both lists and keep appending Node with smaller value to new list
        while l1 and l2:       
            if l1.val < l2.val: #append l1 to new list
                cur.next = l1
                l1 = l1.next                
            else: #append l2 to new list
                cur.next = l2
                l2 = l2.next   
            #move to next node in merged list
            cur = cur.next
        
        #append the remaining elements of non-empty list
        cur.next = l1 or l2      
        
        return dummy.next
        
        
        