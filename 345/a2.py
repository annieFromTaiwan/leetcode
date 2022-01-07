class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = [i for i in range(len(s)) if s[i] in 'aeiouAEIOU']
        for i, j in zip(vowels, vowels[::-1]):
            if i >= j:
                break
            s[i], s[j] = s[j], s[i]
        return ''.join(s)


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = [i for i in range(len(s)) if s[i] in 'aeiouAEIOU']
        for i in range(len(vowels)//2):
            s[vowels[i]], s[vowels[~i]] = s[vowels[~i]], s[vowels[i]]
        return ''.join(s)
