import pickle
from time import time

filename = 'flask_session/6c6d7c1776479ca0ee9896f4dcec9250'


def read_content(filename):
    with open(filename, "rb") as f:
        pickle_time = pickle.load(f)
        return pickle.load(f)

print(read_content(filename))