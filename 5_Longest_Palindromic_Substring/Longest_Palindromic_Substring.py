#!/usr/bin/python

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #sample :fadsgsdyi
     #   maxlen = -1
        if s==None or len(s)==0:
            return ""
        maxLen = 0
        res = ""
        for i in range(0,2*len(s)-1):
            left = i/2
            right = i/2
            if(i%2==1):
                right +=1
            str = self.lengthOfPalindrome(s, left,right)
            if(maxLen<len(str)):
                maxLen = len(str)
                res = str
        return res

    def lengthOfPalindrome(self,s,left, right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

str = 'aadsggsdyi'
sol = Solution()

print(sol.longestPalindrome(str))

