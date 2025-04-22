from LinkedBinaryTree import LinkedBinaryTree
def min_and_max(bin_tree):
    if bin_tree.root == None:
        raise ValueError("Binary tree is empty")
    def subtree_min_and_max(root):
        min_val = root.data
        max_val = root.data
        if root.left != None:
            left_min, left_max = subtree_min_and_max(root.left)
            min_val = min(min_val, left_min)
            max_val = max(max_val, left_max)
        if root.right != None:
            right_min, right_max = subtree_min_and_max(root.right)
            min_val = min(min_val, right_min)
            max_val = max(max_val, right_max)
        return min_val, max_val
    return subtree_min_and_max(bin_tree.root)
