class Solution:
    def goodNodes(self, root):

        def dfs(node, max_value):
            if not node:
                return 0

            count = 0

            # Is this node good?
            if node.val >= max_value:
                count = 1
                max_value = node.val

            count += dfs(node.left, max_value)
            count += dfs(node.right, max_value)

            return count

        return dfs(root, root.val)