class Employee():
    def __init__(self, name: str, lastname: str, position: str):
        self.name = name
        self.lastname = lastname
        self.position = position
        self.subordinates = []
        self.boss = None
        self.id: str = Employee.generate_id(self)

    @staticmethod
    def generate_id(self):
        result = ""
        if(self.name == None or self.lastname == None):
            return result

        if len(self.name) > 3:
            result += self.name[0:3]
        else:
            if len(self.name) <= 3:
                result += self.name[0:2]
                result += "0"

        if len(self.lastname) >= 3:
            result += self.lastname[0:3]
        else:
            result += self.lastname[0:2]
            result += "0"

        result += self.position[0:3]
        return result
    


class Company():
    def __init__(self, root: Employee):
        self.root = root

    @staticmethod
    def insert(root, who, where):
        if (root.position == where):
            root.subordinates.append(who)
            who.boss = root
            return
        for emp in root.subordinates:
            emp.insert(who, where)

    def find_print(self):
        pass


emp0 = Employee ("Олег", "Вершинин", "Директор")
company = Company(emp0)

company.insert(company.root, Employee(None, None, "Курсы"), "Директор")



# print(f'Сотрудник: ({emp1.id}), {emp1.name}, {emp1.lastname}')