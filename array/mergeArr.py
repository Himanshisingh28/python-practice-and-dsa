class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums3=[]
        nums4=[]
        for i in range(m):
            nums3.append(nums1[i])
        for i in range(n):
            nums4.append(nums2[i])
        nums3.extend(nums4)
        nums3.sort()
        for i in range(m + n):
            nums1[i] = nums3[i]
        return nums1
    
        