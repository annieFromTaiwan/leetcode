class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return (p is None and q is None) or (p and q and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
