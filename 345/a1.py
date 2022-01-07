class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = []
        index = []
        for i, c in enumerate(s):
            if c in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                vowels.append(c)
                index.append(i)
        index = index[::-1]
        for i, c in zip(index, vowels):
            s[i] = c
        return ''.join(s)
