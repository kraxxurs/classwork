class Node():
    def __init__(self, value, priority):
        self.left = None
        self.right = None
        self.value = value
        self.priority = priority


class Treap():
    def __init__(self, root, priority):
        self.root = Node(root, priority)

    def insert(self, new_value):
        if (self.value < new_value):
            if(self.right is None):
                self.right = Node(new_value)
            else:
                self.right.insert(new_value)
        
        if (self.value > new_value):
            if(self.left is None):
                self.left = Node(new_value)
            else:
                self.left.insert(new_value)

    def printTree(self, cur_root, level):
        if cur_root is None:
            return
        self.printTree(cur_root.right, level + 1)
        print(f"{'   ' * level} -> {cur_root.value} ({cur_root.count})")
        self.printTree(cur_root.left, level + 1)


tree_root = Treap(50, 0)
tree_root.insert(10, 0)