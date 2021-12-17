class Solution:
    def numSplits(self, s: str) -> int:
        _set = set()
        prefix = [0, ]
        for c in s:
            _set.add(c)
            prefix.append(len(_set))
        prefix = prefix[:-1]
        _set = set()
        suffix = []
        for c in s[::-1]:
            _set.add(c)
            suffix.append(len(_set))
        suffix = suffix[::-1]
        suffix.append(0)
        print(prefix, suffix)
        return sum(a == b for a, b in zip(prefix, suffix))
