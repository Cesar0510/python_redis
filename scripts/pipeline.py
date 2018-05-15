import redis
from timeit import Timer


NUM_OF_USERS = 10_000
KEY_USERS = 'test:users'
KEY_USER = 'test:user:{}'

REPEAT = (7, 1)

r = redis.StrictRedis(
        host='localhost',
        port=6379
    )

def with_pipe(redis=r,func=None):
    p = redis.pipeline()
    func(p)
    p.execute()

def create_users(redis=r):
    for i in range(NUM_OF_USERS):
        redis.lpush(KEY_USERS, i)


setup = """
from __main__ import create_users, with_pipe
"""
stmt = 'create_users()'
print(Timer(stmt,setup).repeat(*REPEAT))
stmt = 'with_pipe(func=create_users)'
print(Timer(stmt,setup).repeat(*REPEAT))

