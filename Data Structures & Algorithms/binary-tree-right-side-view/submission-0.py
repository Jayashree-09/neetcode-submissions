from collections import deque

class Solution:
    def rightSideView(self, root):

        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:

            for i in range(len(queue)):

                node = queue.popleft()

                if i == 0:
                    result.append(node.val)

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)

        return result