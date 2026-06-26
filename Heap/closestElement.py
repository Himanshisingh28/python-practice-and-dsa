import heapq
class Solution(object):
    def distance(self, num,x):
        return abs(x-num)
    def findClosestElements(self, arr, k, x):
        heap=[]

        for i in range(k):
            dist=self.distance(arr[i],x)
            heapq.heappush(heap,(-dist, -arr[i]))

        for i in range(k, len(arr)):
            dist=self.distance(arr[i],x)

            if dist < -heap[0][0] or (dist == -heap[0][0] and arr[i] < -heap[0][1]):
                heapq.heappop(heap)
                heapq.heappush(heap,(-dist, -arr[i]))
        ans=[]
        for dist, num in heap:
            ans.append(-num)
        return sorted(ans)
