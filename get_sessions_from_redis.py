import redis
import pickle

r = redis.StrictRedis()

for key in r.scan_iter("session:*"):
    key_str = key.decode('utf-8')
    ttl_expire_in = r.ttl(key_str)
    print(f'key: {key_str}')
    print(f'expire in sec (ttl): {ttl_expire_in}')
    val = r.get(key_str)
    print(f'val: {val}')
    data = pickle.loads(val)
    print(f'pickle val: {data}')

    
    