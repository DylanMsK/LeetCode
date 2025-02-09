# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        nums = []
        while queue:
            node = queue.pop(0)
            nums.append(node.val)
            left, right = node.left, node.right
            if left:
                queue.append(left)
            if right:
                queue.append(right)
        
        nums.sort()
        result = float("inf")
        for i in range(1, len(nums)):
            result = min(nums[i]-nums[i-1], result)
        return result
            
            

        return result