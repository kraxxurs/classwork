# WH - склад
# PP - пункт выдачи

import csv

products_moves = {}
all_places = set()
not_senders = []

with open("graphy/logistics.csv", newline = "") as file:
    reader = csv.DictReader(file)
    for row in reader:
        sender = row["Отправитель"]
        getter = row["Получатель"]
        count = row["Кол-во_товаров"]
        all_places.add(sender)
        all_places.add(getter)

        if sender in products_moves:
            products_moves[sender].append([getter, count])
        else:
            products_moves[sender] = [[getter, count]]

def find_not_senders():
    for p in all_places:
        if p not in products_moves:
            not_senders.append(p)
    return not_senders

def count_all_products():
    result = 0
    WH = input("Введите номер склада: ")
    for k,v in products_moves.items():
            for row in v:
                if row[0] == WH:
                    result += int(row[1])
    return result

def max_sended_place():
    result = {}
    for k,v in products_moves.items():
        for row in v:
            if k in result:
                result[k] += int(row[1])
            else:
                result[k] = int(row[1])
    

    max = 0
    
                 
                 


#print(find_not_senders())
#print(count_all_products())
print(max_sended_place())