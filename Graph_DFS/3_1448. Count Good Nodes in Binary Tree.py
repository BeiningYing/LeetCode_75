# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

class Solution:
    # def goodNodes(self, root: TreeNode) -> int:
        # if not root:
        #     return 0
        # nums = []
        # nums.append(root.val)
        # def good(root, nums, mx):
        #     mx1 , mx2 = mx, mx
        #     if root.left:
        #         if root.left.val >= mx1:
        #             mx1 = root.left.val
        #             nums.append(root.left.val)
        #         good(root.left, nums, mx1)
        #     if root.right:
        #         if root.right.val >= mx2:
        #             mx2 = root.right.val
        #             nums.append(root.right.val)
        #         good(root.right, nums, mx2)
        #     return nums
        # return len(good(root, nums, root.val))
        
    def goodNodes(self, root: TreeNode, mx=-inf) -> int:
        if root is None:
            return 0
        # 递归并更新mx
        left = self.goodNodes(root.left, max(mx, root.val))
        right = self.goodNodes(root.right, max(mx, root.val))
        # 每次递归判断并增加“好节点”
        return left + right + (root.val >= mx)
