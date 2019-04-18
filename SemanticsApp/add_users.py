import requests

USERS = [
    ['a', 'test1@gmail.com'],
    ['b', 'test2@gmail.com'],
    ['c', 'test3@gmail.com'],
    ['d', 'test4@gmail.com'],
    ['e', 'test5@gmail.com'],
    ['f', 'test6@gmail.com'],
    ['g', 'test7@gmail.com'],
    ['h', 'test8@gmail.com'],
    ['i', 'test9@gmail.com'],
    ['j', 'test0@gmail.com'],
]

for u in USERS:
    a = requests.get("http://127.0.0.1:5000/users/new/%s/%s" % (u[0], u[1]))
    print(a.text)
