import sys


def read_file(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 2:
                raise ValueError('Line doesn\'t contain two ints')
            k = int(parts[0])
            m = int(parts[1])
            break

        for line in f:
            line = line.strip()
            if not line:
                continue
            ids = [int(x) for x in line.split()]
            break
        else:
            ids = []

    if len(ids) != m:
        raise ValueError("m does not match number of requests")

    return k, ids

def fifo(k, requests):
    frames = []
    pfs = 0

    for request in requests:
        if request not in frames:
            pfs += 1
            if len(frames) < k:
                frames.append(request)
            else:
                frames.pop(0)
                frames.append(request)

    return pfs

def lru(k, requests):
    frames = []
    pfs = 0

    for request in requests:
        if request not in frames:
            pfs += 1
            if len(frames) < k:
                frames.append(request)
            else:
                frames.pop(0)
                frames.append(request)
        else:
            frames.remove(request)
            frames.append(request)

    return pfs

def main():
    filename = "ProgAssignment2/testfiles/ex3.txt"

    k, requests = read_file(filename)
    print(f"FIFO: {fifo(k,requests)}")
    print(f"LRU: {lru(k,requests)}")



if __name__ == '__main__':
    main()