from LinkedBinaryTree import LinkedBinaryTree
def is_height_balanced(bin_tree):
    def check_balance(node):
        if node is None:
            return (True, -1)

        left_balanced, left_height = check_balance(node.left)
        right_balanced, right_height = check_balance(node.right)

        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

        height = max(left_height, right_height) + 1
        return (balanced, height)

    return check_balance(bin_tree.root)[0]



