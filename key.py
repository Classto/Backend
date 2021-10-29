from time import time
from random import random
import hashlib

def new_id():
    id = int(str(round(time())) + str(round((random() * 1000000))))
    return id

def to_hash(data):
    return hashlib.sha224(bytes(data, "utf-8")).hexdigest()

if __name__ == "__main__":
    a = new_id()
    for _ in range(10000):
        b = new_id() 
        if b == a:
            print("oops")
            break
        print(f"attemp: {_}, {b}")