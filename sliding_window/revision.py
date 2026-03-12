class Solution:
    def longestKSubstr(self, s, k):
        n=len(s)
        left=0
        freq={}
        res=-1
        for right in range(n):
            freq[s[right]]=freq.get(s[right],0)+1
            while len(freq)>k:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
            if len(freq)==k:
                res=max(res,right-left+1)
                
        return res
        


        
class Solution(object):
    def totalFruit(self, fruits):
        left=0
        freq={}
        max_len=0
        for right in range(len(fruits)):
            fruit=fruits[right]
            freq[fruit]=freq.get(fruit,0)+1

            while len(freq)>2:
                freq[fruits[left]]-=1
                if freq[fruits[left]]==0:
                    del freq[fruits[left]]
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len
        

class Solution(object):
    def minSubArrayLen(self, target, nums):
        low=0
        high=0
        window_sum=0
        n=len(nums)
        res=float('inf')
        for high in range(0,n):

            window_sum=window_sum+nums[high]

            while window_sum>=target:
                len1=high-low+1
                res=min(res,len1)
                window_sum=window_sum-nums[low]
                low+=1
            high+=1
        if res==float('inf'):
            return 0
        return res
















