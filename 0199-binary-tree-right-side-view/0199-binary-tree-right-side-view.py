# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is not None:
            queue = [root]
            while queue:
                length = len(queue)
                nums = []
                for _ in range(length):
                    node = queue.pop(0)
                    nums.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                if nums:
                    result.append(nums[-1])
        return result

