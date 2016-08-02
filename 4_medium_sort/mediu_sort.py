#!/usr/bin/python

class Solution(object):
    def popmini(self,nums1,nums2):
        if(nums1==None or len(nums1)==0) and (nums2==None or len(nums2)==0):
            return None
        elif(nums1==None or len(nums1)==0):
            return nums2.pop(0)
        elif(nums2==None or len(nums2)==0):
            return nums1.pop(0)
        else:
            if(nums1[0]<nums2[0]):
                return nums1.pop(0)
            else:
                return nums2.pop(0)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if(nums1 == None or len(nums1) == 0) and (nums2 == None or len(nums2) == 0):
            return 0
        elif (nums1 == None or len(nums1) == 0):
            if(len(nums2)%2==0):
                return (nums2[len(nums2)/2-1]+nums2[len(nums2)/2])/2.0
            else:
                return nums2[len(nums2)/2]
        elif (nums2 == None or len(nums2) == 0):
            if (len(nums1) % 2 == 0):
                return (nums1[len(nums1) / 2 - 1] + nums1[len(nums1)/2]) / 2.0
            else:
                return nums1[len(nums1) / 2]

        totalSize = len(nums1)+len(nums2)
        result = []
        if(totalSize%2==0):
            leftcount = totalSize/2-1
        else:
            leftcount = totalSize/2

        cnt = 0
        while(len(nums1)>0 or len(nums2)>0):
            if(cnt==leftcount):
                break;
            self.popmini(nums1,nums2)
            cnt += 1


        if(totalSize%2==0):
            result.append(self.popmini(nums1,nums2))
            result.append(self.popmini(nums1, nums2))
            return (result[0]+result[1])/2.0
        else:
            return self.popmini(nums1,nums2)





sol = Solution()
nums1=[1,1]
nums2=[1,1]
target = 1
print(sol.findMedianSortedArrays(nums1,nums2))



