class Solution:
    def goodNodes(self, root):

        def dfs(node, maxVal):

            if not node:
                return 0

            count = 0

            if node.val >= maxVal:
                count = 1

            maxVal = max(maxVal, node.val)

            count += dfs(node.left, maxVal)
            count += dfs(node.right, maxVal)

            return count

        return dfs(root, float('-inf'))