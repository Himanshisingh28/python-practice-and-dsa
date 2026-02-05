class Solution(object):
    def findDifference(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)

        new = []
        for x in set1:
            if x not in set2:
                new.append(x)

        new1 = []
        for x in set2:
            if x not in set1:
                new1.append(x)

        return [new, new1]