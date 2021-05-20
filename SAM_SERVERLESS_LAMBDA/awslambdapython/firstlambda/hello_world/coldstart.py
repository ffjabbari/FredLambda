import json
import random

global_random_var = random.random()

def cold_start(event, context):
    local_random_var = random.random()
    print(global_random_var)
    print(local_random_var)
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa2')