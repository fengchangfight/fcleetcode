class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        originSize = len(nums)
        endIndex = originSize-1
        while(endIndex>=0):
            if (target - nums[endIndex] in nums[0:endIndex]):
                result.append(endIndex)
                result.insert(0, nums[0:endIndex].index(target - nums[endIndex]))
                return result
            else:
                endIndex -= 1
        return None
