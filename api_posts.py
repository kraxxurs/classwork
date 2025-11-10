import requests
import json

def save(path, collection):
    with open (path, 'w', encoding = 'utf-8') as file:
        json.dump(collection, file, ensure_ascii = False, indent = 2)


url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)
print(response.status_code)
# print(response.json())

save('users.json', response.json())


class Post():
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body

    def to_dict(self):
        return self.__dict__.copy()
    

class User():
    def __init__(self, id, name, address, phone):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        self.posts = self._load_posts()

    def _load_posts(self):
        params = {'userID': self.id}
        url = 'https://jsonplaceholder.typicode.com/posts'
        response = requests.get(url, params = params)
        posts = []
        for post in response.json():
            posts.append(Post(post['id'],
                              post['title'],
                              post['body']))
        return posts

    @staticmethod
    def create_user(user_dict):
        address = f"{user_dict['address']['street']} {user_dict['address']['suite']}"
        return User(user_dict['id'],
                    user_dict['name'],
                    address,
                    user_dict['phone'])
    
    def to_dict(self):
        result = self.__dict__.copy()
        result['posts'] = [post.to_dict() for post in self.posts]
        return result
    
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)
users_obj = []
for user in response.json():
    users_obj.append(User.create_user(user))

users_dict = []
for user in users_obj:
    users_dict.append(user.to_dict())

save('users_posts.json', users_dict)
