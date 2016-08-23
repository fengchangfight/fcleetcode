#!/usr/bin/python

class Solution(object):
    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        ss = ''
        if(x>=0):
            ss = str(x)
            return int(ss[::-1])
        else:
            ss= str(x)[1:len(str(x))]
            ss='-'+ss[::-1]
            return int(ss)



    def reverse(self, x):
        reverse_digits = []
        i = abs(x)
        while i > 0:
            reverse_digits.append(i % 10)
            i = i / 10
        sum = 0
        for j in range(len(reverse_digits)):
            sum += reverse_digits[j] * (10 ** (len(reverse_digits) - j - 1))
        if sum > (2 ** 31) - 1: return 0
        return sum if x > 0 else -1 * sum

sol = Solution()
print(sol.reverse2(1534236469))