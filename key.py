from time import time
from random import random
import hashlib

def new_id():
    id = int(str(round(time())) + str(round((random() * 1000000))))
    return id

def to_hash(data):
    return hashlib.sha224(bytes(data, "utf-8")).hexdigest()
