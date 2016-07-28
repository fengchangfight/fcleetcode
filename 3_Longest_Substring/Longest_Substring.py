#!/usr/bin/python

class Solution(object):
    def containsDuplicate(self,s):
        return not (len(s)==len(set(s)))
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(s == None):
            return None
        if(len(s) == 1):
            return len(s)

        i = 0
        result = s[0:1]

        i+=1
        while(i<len(s)):
            if(not self.containsDuplicate(s[i-len(result):i+1])):
                k = 0
                while(k<=i-len(result)):
                    if(not self.containsDuplicate(s[k:i+1])):
                        result = s[k:i+1]
                        break
                    k+=1
            i+=1
        return len(result)

sol = Solution()
print(sol.lengthOfLongestSubstring("c"))