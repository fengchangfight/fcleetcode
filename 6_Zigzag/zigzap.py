#!/usr/bin/python


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(numRows==1):
            return s
        outerlist = []
        result=''
        inc = True
        line = 0

        for k in range(0,numRows):
            list = []
            outerlist.append(list)
        for i in range(0,len(s)):
            outerlist[line].append(s[i])
            if(line==numRows-1):
                inc = False
            if(line == 0):
                inc = True
            if(inc):
                line += 1
            else:
                line -=1
        for j in range(0, numRows):
            result+=''.join(outerlist[j])
        return result

sol = Solution()
print(sol.convert("ab",1))
