class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None
        self.height = 1
    
class AVL:
    def __init__(self):
        self.root = None

    def printTree(self, root, level):
        if root is None:
            return
        self.printTree(root.right, level + 1)
        print("   " * level, "->", root.value)
        self.printTree(root.left, level + 1)

    def insert(self, new_value):
        def _insert(node: Node, new_value: int):
            if(node is None):
                return Node(new_value)
            elif (node.value < new_value):
                node.right = _insert(node.right, new_value)
            else:
                node.left = _insert(node.left, new_value)

            node.height = max(self.getHeight(node.right),
                              self.getHeight(node.left)) + 1

            return self.rotate(node, new_value)

        self.root = _insert(self.root, new_value)

    def rotate(self, node, new_value):
        balance = self.getHeight(node.left) - self.getHeight(node.right)
        
        if(balance > 1 and new_value < node.left.value):
            return self.rightRotate(node)
        
        elif(balance > 1 and new_value > node.left.value):
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        
        elif(balance < -1 and new_value > node.right.value):
            return self.leftRotate(node)
        
        elif(balance < -1 and new_value < node.right.value):
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node
    

    def rightRotate(self, node):
        left_child = node.left
        left_child_right = left_child.right
        left_child.right = node
        node.left = left_child_right

        node.height = max(self.getHeight(node.right),
                        self.getHeight(node.left)) + 1
        
        left_child.height = max(self.getHeight(left_child.right),
                            self.getHeight(left_child.left)) + 1
        return left_child

    def leftRotate(self, node):
        right_child = node.right
        right_child_left = right_child.left
        right_child.left = node
        node.right = right_child_left

        node.height = max(self.getHeight(node.right),
                        self.getHeight(node.left)) + 1
        
        right_child.height = max(self.getHeight(right_child.right),
                            self.getHeight(right_child.left)) + 1
        return right_child

    def getHeight(self, node):
        if(node is None):
            return 0
        return node.height
    
    def delete(self, root, del_value):
        # 1. нет узла
        if(root is None):
            return None
        # поиск узла
        if(root.value < del_value):
            root.right = self.delete(root.right, del_value)
        elif (root.value > del_value):
            root.left = self.delete(root.left, del_value)
        else:
            # нашли узел
            # 2. нет дочерних элементов
            if(root.left is None and root.right is None):
                return None
            # 3. два дочерних элемента
            elif(root.left and root.right):
                nodeMax = self.findMax(root.left)
                root.value = nodeMax.value
                root.left = self.delete(root.left, nodeMax.value)
            # 4. один дочерний элемент
            else:
                root = root.left if root.left else root.right
        return self.rotate(root, del_value)
    
    def findMax(self, root):
        while root.right:
            root = root.right
        return root

avl = AVL()
avl.root = Node(50)
avl.insert(20)
avl.insert(30)
avl.printTree(avl.root, 0)

avl.delete(avl.root, 30)
avl.printTree(avl.root, 0)