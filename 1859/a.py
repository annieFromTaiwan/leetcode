class Solution:
    def sortSentence(self, s: str) -> str:
        words = [w[:-1] for w in sorted(s.split(), key=lambda w: w[-1])]
        return ' '.join(words)
      
class Solution2:
    def sortSentence(self, s: str) -> str:
        tuples = sorted([(word[-1], word[:-1]) for word in s.split(' ')])
        return ' '.join(t[1] for t in tuples)
