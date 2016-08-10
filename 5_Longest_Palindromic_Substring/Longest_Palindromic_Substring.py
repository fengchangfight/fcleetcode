#!/usr/bin/python

class Solution(object):
    def isPalindrome(self,s,start,end):
        while(end>=start):
            if(s[start]==s[end]):
                start += 1
                end -= 1
                continue
            else:
                return False
        return True

    def containsPalindromeOfLengthK(self,s,k):
        if(k>=1 and k<=len(s)):
            for i in range(0,len(s)-k+1) :
                if(self.isPalindrome(s,i,i+k-1)):
                    return s[i:i+k]
            return False
        else:
            return False
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #sample :fadsgsdyi
        maxlen = -1
        for i in range(0, len(s)):
            result = self.containsPalindromeOfLengthK(s,len(s)-i)
            if(result):
                return result
        return None

str = 'aadsggsdyi'
sol = Solution()

print(sol.longestPalindrome(str))

