import time

def rando(seed, multiplier, increment, remainder, lis_length):
    result = []
    for i in range(lis_length):
        seed = (multiplier * seed + increment) % remainder
        result.append(seed)
    return result





if __name__=='__main__':
    time_secs = int(time.strftime('%S'))

    print(rando(time_secs, 2, 2, 3, 10))