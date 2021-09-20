from heapq import heappush, heappop, heapify
from collections import Counter
class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

class Solution(object):
    def topKFrequent(self, words):
        counts = Counter(words)
        dic = dict()

        heap = []
        for word, count in counts.items():
            elem = Element(count, word)
            dic[word] = elem
            heappush(heap, elem)

        dic["leetcode"].count += 10
        heapify(heap)
        while heap:            
            elem = heappop(heap)
            print(elem.word, elem.count)


words = ["i","love","leetcode","i","love","coding"]
s = Solution()
s.topKFrequent(words)