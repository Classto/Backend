from time import time
from random import random
import hashlib

async def new_id():
    id = int(str(round(time())) + str(round((random() * 1000000))))
    return id

async def to_hash(data):
    hashlib.sha224(bytes(data, "utf-8")).hexdigest()
