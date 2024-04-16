# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # 创建2个数组放叶子
        num1, num2 = [], []
        # 递归
        def leaf(root, numbers):
            if root.left:
                leaf(root.left, numbers)
            if root.right:
                leaf(root.right, numbers)
            # 既没有左又没有右，那就是叶子
            elif not root.left:
                numbers.append(root.val)
            return numbers
        # 返回
        return leaf(root1, num1) == leaf(root2, num2)