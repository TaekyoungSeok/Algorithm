class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class CompleteBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = TreeNode(key)

        if self.root is None:
            self.root = new_node
            return new_node

        queue = [self.root]

        while queue:
            node = queue.pop(0)

            if node.left is None:
                node.left = new_node
                return new_node

            if node.right is None:
                node.right = new_node
                return new_node

            queue.append(node.left)
            queue.append(node.right)

    def level_order(self):
        result = []

        if self.root is None:
            return result

        queue = [self.root]

        while queue:
            node = queue.pop(0)
            result.append(node.key)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return result

    def tree_to_array(self):
        if self.root is None:
            return []

        array = []
        queue = [(self.root, 0)]

        while queue:
            node, index = queue.pop(0)

            if index >= len(array):
                array.extend([None] * (index - len(array) + 1))

            array[index] = node.key

            if node.left is not None:
                queue.append((node.left, 2 * index + 1))

            if node.right is not None:
                queue.append((node.right, 2 * index + 2))

        return array

if __name__ == "__main__":
    tree = CompleteBinaryTree()

    for key in [10, 20, 30, 40, 50, 60]:
        tree.insert(key)

    print("레벨 순회 : ", tree.level_order())

    print("루트:", tree.root.key)
    print("루트의 왼쪽 자식:", tree.root.left.key)
    print("루트의 오른쪽 자식:", tree.root.right.key)

    array_representation = tree.tree_to_array()
    print("배열 표현법으로 변경 시 : ", array_representation)