class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        for i in range(0,size-1):
            for j in range(i+1,size):
                if(nums[i]+nums[j]==target):
                    return [i,j]

sol = Solution()
nums = [1,2,7,9]
target = 9
print(sol.twoSum(nums,target));