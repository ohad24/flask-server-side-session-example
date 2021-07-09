from hashlib import md5
session_cookie_value = 'c2c9cc6c-5cba-4372-859d-ab8662266460'
s = 'session:' + session_cookie_value

def _get_filename(key):
    if isinstance(key, str):
        key = key.encode("utf-8")  # XXX unicode review
    hash = md5(key).hexdigest()
    return hash

print(_get_filename(s))