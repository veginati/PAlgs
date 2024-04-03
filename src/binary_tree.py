# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.helper(preorder, inorder)

    def helper(self, preorder, inorder):
        stack_obj = []
        root = None
        add_left=True
        prev_node= None
        in_order_index=0
        for i in range(len(preorder)):
            curr_node = TreeNode(preorder[i])

            if not root:
                root = curr_node

            while len(stack_obj)>0 and stack_obj[-1].val == inorder[in_order_index]:
                prev_node = stack_obj.pop()
                add_left=False
                in_order_index+=1

            if prev_node and add_left:
                prev_node.left=curr_node
            elif prev_node:
                prev_node.right=curr_node
                add_left=True

            stack_obj.append(curr_node)
            prev_node=curr_node

        return root

if __name__ == '__main__':
    obj = Solution()
    obj.buildTree([3,9,20,15,7],[9,3,15,20,7])
