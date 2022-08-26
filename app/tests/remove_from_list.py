list = [
    {
        'a': 1,
        'b': 1
    },
    {
        'a': 2,
        'b': 2
    },
    {
        'a': 3,
        'b': 3
    },
    {
        'a': 4,
        'b': 4
    },
]

def check_post_id(post_id):
    for post in list:
        if post['a'] == post_id:
            list.remove(post)

check_post_id(3)
print(list)