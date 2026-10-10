class ArrayBinaryTree:
    def __init__(self, height):
        self.array = [None] * (2 ** height - 1)

    def set_node(self, index, data):
        if index < 0 or index >= len(self.array):
            raise ValueError("배열의 범위를 벗어났습니다.")

        if index > 0:
            parent_index = (index - 1) // 2

            if self.array[parent_index] is None:
                raise ValueError("부모 노드가 없습니다.")

        self.array[index] = data

if __name__ == "__main__":
    tree = ArrayBinaryTree(3)

    tree.set_node(0, 10)
    tree.set_node(1, 20)
    tree.set_node(2, 30)
    tree.set_node(4, 40)

    print(tree.array)