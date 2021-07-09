# import base64
from itsdangerous import base64_decode
import json
import zlib
from pprint import pprint

cookie='.eJwlzjsOwjAMANC7ZGZw7Nhue5kq_gnWlk6Iu1OJ_Q3v0_Y68ny27X1c-Wj7K9rWFDpKeqXbDFFUQnDESb2Ci7DUjE0nItJESB7C2m_oE3mRADCyKB-jaznBEpKGvYqUjZnmCmlehtEpTIRpyJqLALOFlrQ7cp15_De9fX_DCy9H.YOhGEw.iFmf1XmD2BfNZHv-MgCdTJ-F9TU'
# c='eyJfZnJlc2giOmZhbHNlLCJfcGVybWFuZW50Ijp0cnVlLCJ0IjoxNjI1ODQxODYxLjE2NTgwNDl9.YOhgxQ.KxBTB4f6OtoeDh1eOPSTy59lqi8'
compressed = False
if cookie.startswith('.'):
    compressed = True
    cookie = cookie[1:]

data = cookie.split(".")[0]

data = base64_decode(data)
if compressed:
    data = zlib.decompress(data)

data = data.decode('utf-8')
pprint(json.loads(data))