class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l, r = 0, len(s) - 1
        target = 'aeiouAEIOU'
        while l < r:
            if s[l] not in target:
                l += 1
                continue
            if s[r] not in target:
                r -= 1
                continue
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)


class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        s = list(s)
        vowels = 'aeiouAEIOU'
        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            if s[l] not in vowels:
                l += 1
            if s[r] not in vowels:
                r -= 1
        return ''.join(s)
