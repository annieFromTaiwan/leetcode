import heapq
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        return min(b-a for a, b in zip(heapq.nsmallest(4, nums), heapq.nlargest(4, nums)[::-1]))
