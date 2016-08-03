#!/usr/bin/python

class Solution(object):
    def palindromeatpoint(self, s, index):
        if(s==None or len(s)==0 or index<0 or index>=len(s)):
            return None
        i=j=1
        oddsize = 1
        while(index-i>=0 and index+i<len(s)):
            if(s[index-i]==s[index+i]):
                oddsize+=2
                i += 1
            else:
                break
        if(index<len(s)-1 and s[index]==s[index+1]):
            evensize = 2
            while (index - j >= 0 and index + 1 + j < len(s)):
                if (s[index - j] == s[index + 1 + j]):
                    evensize += 2
                    j += 1
                else:
                    break
        else:
            evensize = -1
        if(evensize > oddsize):
            start = index - j + 1
            return s[start:start+evensize]
        else:
            start = index - i + 1
            return s[start:start+oddsize]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #sample :fadsgsdyi
        maxlen = -1
        for i in range(0, len(s)):
            sub = self.palindromeatpoint(s,i)
            if(len(sub)>maxlen):
                maxlen=len(sub)
                result = sub
        return result



str = 'aadsggsdyi'
sol = Solution()




print(sol.longestPalindrome(str))

