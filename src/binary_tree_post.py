from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    curr_index = -1

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = dict()
        self.curr_index = len(inorder) - 1
        for index, val in enumerate(inorder):
            inorder_map[val] = index
        return self.helper(0, len(inorder) - 1, postorder, inorder, inorder_map)

    def helper(self, left, right, postorder, inorder, inorder_map):
        if left > right:
            return None
        # print(self.curr_index)
        curr_node = TreeNode(postorder[self.curr_index])
        self.curr_index -= 1
        curr_node.right = self.helper(inorder_map[curr_node.val] + 1, right, postorder, inorder, inorder_map)
        curr_node.left = self.helper(left, inorder_map[curr_node.val] - 1, postorder, inorder, inorder_map)
        return curr_node