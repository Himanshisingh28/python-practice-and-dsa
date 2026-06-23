import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):

        freq = Counter(words)

        heap = []

        for word, count in freq.items():
            heapq.heappush(heap, (-count, word))

        ans = []

        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans