class Solution(object):
    def intersection(self, nums1, nums2):
      new=[]
      set1=set(nums1)
      set2=set(nums2)
      for x in set1:
        if x in set2:
            new.append(x)
      return new
        