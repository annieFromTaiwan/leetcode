class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outward = Counter([a for a, b in trust])
        inward = Counter([b for a, b in trust])
        for i in range(1, n+1):
            if outward[i] == 0 and inward[i] == n-1:
                return i
        return -1
