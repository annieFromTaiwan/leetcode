class Solution:
    def numSplits(self, s: str) -> int:
        def calc(s):
            _set = set()
            count = []
            for c in s:
                _set.add(c)
                count.append(len(_set))
            return count[:-1]
        return sum(a == b for a, b in zip(calc(s), calc(s[::-1])[::-1]))
