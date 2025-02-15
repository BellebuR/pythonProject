class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

# Пример использования
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
root.add_child(child1)
root.add_child(child2)

# Для проверки, что дерево создано, можно вывести значения
print(root.value)  # Вывод: 1
print([child.value for child in root.children])  # Вывод: [2, 3]