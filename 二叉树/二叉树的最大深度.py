from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def get_depth(root: TreeNode) -> int:
            # 深度优先遍历
            if root is None:
                return 0
            left_depth = get_depth(root.left)
            right_depth = get_depth(root.right)
            return max(left_depth, right_depth) + 1

        return get_depth(root)


"""
广度优先遍历
from collections import deque
from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = deque([root])
        ans = 0
        
        while q:  # 当队列不为空时继续
            ans += 1
            # 处理当前层的所有节点
            for _ in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return ans
"""