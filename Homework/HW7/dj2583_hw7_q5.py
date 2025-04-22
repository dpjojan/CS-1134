from LinkedBinaryTree import LinkedBinaryTree

def create_expression_tree(prefix_exp_str):
    tokens = prefix_exp_str.split()

    def helper(start_pos):
        token = tokens[start_pos]
        if token in '+-*/':
            node = LinkedBinaryTree.Node(token)
            left_subtree, left_size = helper(start_pos + 1)
            right_subtree, right_size = helper(start_pos + 1 + left_size)
            node.left = left_subtree
            node.right = right_subtree
            subtree_size = 1 + left_size + right_size
            return node, subtree_size
        else:
            return LinkedBinaryTree.Node(int(token)), 1

    tree = LinkedBinaryTree()
    root_with_size = helper(0)
    tree.root = root_with_size[0]
    tree.size = tree.count_nodes()
    return tree


def prefix_to_postfix(prefix_exp_str):
    tokens = prefix_exp_str.split()

    def helper(start_pos):
        token = tokens[start_pos]
        if token in '+-*/':
            left_subexp, left_size = helper(start_pos + 1)
            right_subexp, right_size = helper(start_pos + 1 + left_size)
            postfix_exp = f"{left_subexp} {right_subexp} {token}"
            total_size = 1 + left_size + right_size
            return postfix_exp, total_size
        else:
            return token, 1

    tree_info = helper(0)
    postfix_exp = tree_info[0]
    return postfix_exp

