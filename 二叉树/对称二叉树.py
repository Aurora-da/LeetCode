from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """递归"""
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self._isMirror(root.left, root.right)

    def _isMirror(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True

        if not left or not right:
            return False

        return (left.val == right.val and
                self._isMirror(left.left, right.right) and
                self._isMirror(left.right, right.left))

"""
广度优先遍历 + 反转数组
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = deque([root])
        while queue:
            level_vals = []

            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    level_vals.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    level_vals.append(None)

            if level_vals != level_vals[::-1]:
                return False

        return True
"""