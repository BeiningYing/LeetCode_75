# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level, max_level, max_sum = 0, 0, -inf
        while queue:
            sum = 0
            length = len(queue)
            level += 1
            for _ in range(length):
                node = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if sum > max_sum:
                max_sum = sum
                max_level = level
        return  max_level