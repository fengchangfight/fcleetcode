#!/usr/bin/python

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1=[]
        stack2=[]
        result = None
        h1 = l1
        h2 = l2
        while(h1!=None):
            stack1.append(h1.val)
            h1=h1.next
        while (h2 != None):
            stack1.append(h2.val)
            h2 = h2.next
        overflowflag = False
        while(len(stack1)>0 and len(stack2)>0):
            tmpadd = stack1.pop()+stack2.pop()

