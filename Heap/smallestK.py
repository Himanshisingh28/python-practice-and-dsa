# class Solution:
#     import heapq
#     def kthSmallest(self, arr, k):
#         # Code here
#         n=len(arr)
#         pq=[]
        
#         for i in range(k):
#             heapq.heappush(pq, -arr[i])
#         for i in range(k,n):
#             if arr[i]>=-pq[0]:
#                 continue
#             heapq.heappop(pq)
#             heapq.heappush(pq, -arr[i])
#         return -pq[0]
            
        
