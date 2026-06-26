import heapq
class Solution(object):
    def distance(self, point):
        x=point[0]
        y=point[1]

        return (x*x + y*y)

    def kClosest(self, points, k):
        n=len(points)
        heap=[]

        for i in range(k):
            dist=self.distance(points[i])
            heapq.heappush(heap,(-dist,points[i]))

        for i in range(k,n):
                dist=self.distance(points[i])
                if dist<-heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,(-dist,points[i]))
        
        ans=[]

        for dist, point in heap:
            ans.append(point)
        return ans       