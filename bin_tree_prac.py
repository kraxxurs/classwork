class Node:
    def __init__(self, value, count = 1):
        self.left = None
        self.right = None
        self.value = value
        self.count = count
        value_list = []
    
    def insert(self, new_value):
        if (self.value < new_value):
            if(self.right is None):
                self.right = Node(new_value)
            else:
                self.right.insert(new_value)
        
        elif(self.value > new_value):
            if(self.left is None):
                self.left = Node(new_value)
            else:
                self.left.insert(new_value)

        else:
            self.count += 1

        root.value_list.append(new_value)

    # DFS - проход в глубину (центрированный)
    def printTree(self, cur_root, level):
        if cur_root is None:
            return
        self.printTree(cur_root.right, level + 1)
        print(f"{'   ' * level} -> {cur_root.value} ({cur_root.count})")
        self.printTree(cur_root.left, level + 1)

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
    
    def average(self, root):
        sum_value = 0
        for i in range(len(root.value_list)):
            sum_value += root.value_list[i]
        print(sum_value / len(root.value_list))


root = Node(50)
root.insert(70)
root.insert(25)
root.insert(90)
root.insert(80)
root.insert(60)
root.insert(30)

root.insert(30)
root.insert(25)
root.insert(90)

root.printTree(root, 0)
root.printDoubles(root, 0)