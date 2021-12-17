from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        suffix = Counter(s)
        prefix = set()
        ans = 0
        for c in s:
            prefix.add(c)
            suffix[c] -= 1
            if suffix[c] == 0:
                suffix.pop(c)
            ans += (len(prefix) == len(suffix))
        return ans
