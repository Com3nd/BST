from typing import Optional


class TreeNode:
    def __init__(self, value):
        self.left: Optional[TreeNode] = None  # Left is less than
        self.right: Optional[TreeNode] = None  # right is greater than
        self.value = value

    def insert(self, value, node: Optional['TreeNode'] = None):
        if node is None:
            node = self
        if not node.left:
            if value < node.value:
                node.left = TreeNode(value)
                return
        elif value < node.value:
            self.insert(value, node.left)

        if not node.right:
            if value > node.value:
                node.right = TreeNode(value)
                return
        elif value > node.value:
            self.insert(value, node.right)

    def inorder_traversal(self, result: list | None = None):
        if result is None:
            result = []

        if self.left:
            self.left.inorder_traversal(result)
        # print(self.value)
        result.append(self.value)
        if self.right:
            self.right.inorder_traversal(result)
        return result


if __name__ == '__main__':
    tree = TreeNode(6)
    tree.insert(5)
    tree.insert(2)
    tree.insert(4)
    tree.insert(1)
    tree.insert(2)
    tree.insert(4)
    tree.insert(19)
    tree.insert(29)
    tree.insert(11)
    tree.insert(4)
    tree.insert(2)
    print(tree.inorder_traversal())
    print(tree.inorder_traversal())
