"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        cur = dummy
        carry = 0
        p1, p2 = l1, l2
        #loop till both lists are empty
        while p1 or p2:
            #get next pair of digits to add
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0       
            
            add = val1 + val2 + carry  #add digits with with input carry            
            cur.next = ListNode(add%10) #create a new node with LSB of sum
            carry = add//10 #get output carry
            cur = cur.next #move to next node
            #advance input lists pointer
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        #if there is final output carry, then add a new node at the end of list    
        if carry:
            cur.next = ListNode(1)
        return dummy.next
    