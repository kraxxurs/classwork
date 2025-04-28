import json
from collections import defaultdict

userA = "0"

with open("graphy/task3.json", "r", encoding = "utf-8") as file:
    users: dict[int, list]  = json.load(file)

# for i in range(len(users)):
#     if users.keys() == userA:
#         userA_friends = [users.values()]

recomendation = {}
for friend in users[userA]:
    
    friend = str(friend)
    for f in users[friend]:
        f = str(f)
        if(f in recomendation):
            recomendation[f] += 1
        else:
            recomendation[f] = 1


print(recomendation)