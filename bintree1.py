class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def insert(self, new_value):
        if (self.value < new_value):
            if(self.right is None):
                self.right = Node(new_value)
            else:
                self.right.insert(new_value)
        else:
            if(self.left is None):
                self.left = Node(new_value)
            else:
                self.left.insert(new_value)
    

    # DFS - проход в глубину (центрированный)
    def printTree(self, root, level):
        if root is None:
            return
        self.printTree(root.right, level + 1)
        print("   " * level, "->", root.value)
        self.printTree(root.left, level + 1)

    def delete(self, root, del_value):
        # 1. нет узла
        if (root is None):
            return None
        # поиск узла
        if (root.value < del_value):
            root.right = root.delete(root.right, del_value)
        elif (root.value > del_value):
            root.left = root.delete(root.left, del_value)
        else:
            # нашли узел
            # 2. нет дочерних элементов
            if(root.left is None and root.right is None):
                return None
            # 3. есть 2 дочерних элемента
            elif (root.left and root.right):
                nodeMax = self.findMax(root.left)
                root.value = nodeMax.value
                root.left = root.delete(root.left, nodeMax.value)
            # 4. есть только один дочерний элемент
            else:
                root = root.left if root.left else root.right
        return root

    def findMax(self,root):
        while root.right:
            root.root.right
        return root


root = Node(50)
root.insert(70)
root.insert(25)
root.insert(90)
root.insert(80)
root.insert(60)
root.insert(30)
root.insert(10)
root.insert(5)
root.insert(58)
root.printTree(root, 0)
print('\n')
root.delete(root, 25)
