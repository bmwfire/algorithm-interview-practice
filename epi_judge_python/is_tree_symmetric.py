from test_framework import generic_test


def is_symmetric(tree):
    def check_symmetric(subtree_0, subtee_1):
        if not subtree_0 and not subtee_1:
            return True
        elif subtree_0 and subtee_1:
            return (subtree_0.data == subtee_1.data
                    and check_symmetric(subtree_0.left, subtee_1.right)
                    and check_symmetric(subtree_0.right, subtee_1.left))
        return False

    return not tree or check_symmetric(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
