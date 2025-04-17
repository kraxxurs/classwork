class CategoryNode():
    def __init__(self, name: str):
        self.name = name
        self.children: list[CategoryNode] = []
        self.products: list[str] = []
        category_list.append(self)

    def add_subcategory(self, node: 'CategoryNode') -> None:
        self.children.append(node)
        category_list.append(node)

    def remove_subcategory(self, name: str) -> bool:
        for i in range(len(self.children)):
            if self.children[i] == name:
                self.children.pop(i)
                self.children[i].children = []
                return True
            else:
                return False

    def add_product(self, product_name: str) -> None:
        self.products.append(product_name)

    def remove_product(self, product_name: str) -> bool:
        for i in range(len(self.products)):
            if self.products[i] == product_name:
                self.products.pop(i)
                self.products[i].products = []
                return True
            else:
                return False


class Pruductcatalog():
    def __init__(self, root):
        self.root = CategoryNode(root)

    def add_category(self, category_name: str, parent_name: str) -> bool:
        for i in range(len(category_list)):
            if category_list[i] == parent_name:
                category_list[i].children.remove(category_name)
                category_list.remove(category_name)

    def remove_category(self, category_name: str, parent_name: str) -> bool:
        for i in range(len(category_list)):
            if category_list[i] == parent_name:
                category_list[i].children.append(CategoryNode(category_name))
                category_list.append(CategoryNode(category_name))

    def add_product(self, product_name: str, category_name: str) -> bool:
        pass

    def remove_product(self, product_name: str, category_name: str) -> bool:
        pass

    def list_products(self, category_name: str, recursive: bool = False) -> list[str]:
        pass

    def move_category(self, category_name: str, new_parent_name: str) -> bool:
        pass

    def print_catalog(self, level) -> None:
        if self.root is None:
            return
        
category_list: list[CategoryNode] = []

category1 = CategoryNode("Одежда")
category1.add_subcategory(CategoryNode("Футболки"))