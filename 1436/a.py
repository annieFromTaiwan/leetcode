class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = set(p[0] for p in paths)
        dest = set(p[1] for p in paths)
        return list(dest - start)[0]
