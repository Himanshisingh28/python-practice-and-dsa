stack = []

stack.append(10)  # push
stack.append(20)

print(stack.pop())  # pop
print(stack[-1])    # peek

class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        
        return res