class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result = None
        tail = None
        h1 = l1
        h2 = l2
        overflowflag = False
        overflowvalue = 0
        while(h1!=None or h2!=None):
            if(h1!=None and h2!=None):
                tmpadd = h1.val + h2.val + overflowvalue
            elif(h1 == None and h2!=None):
                tmpadd = h2.val + overflowvalue
            elif(h1!=None and h2 == None):
                tmpadd = h1.val + overflowvalue
            if(tmpadd >= 10):
                overflowflag = True
                overflowvalue = tmpadd/10
                tmpadd = tmpadd % 10
            else:
                overflowflag = False
                overflowvalue = 0
            if(result == None):
                result = ListNode(tmpadd)
                tail = result
            else:
                tail.next = ListNode(tmpadd)
                tail = tail.next
            if(h1!=None):
                h1 = h1.next
            if(h2!=None):
                h2 = h2.next
        if(overflowflag):
            tail.next = ListNode(overflowvalue)
        return result