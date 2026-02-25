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

def optff(k, requests):
    frames = []
    pfs = 0
    n = len(requests)

    # if its a hit
    for i, request in enumerate(requests):
        if request in frames:
            continue

        # checking if its a miss
        pfs += 1

        # empty slot if avail
        if len(frames) < k:
            frames.append(request)
            continue

        # if the cache is full
        # have to get frame who their next use is farthest away in future
        chosen_frame = None
        farthest_frame = -1

        for idx, page in enumerate(frames):
            used_next = None
            for j in range(i + 1, n):
                if requests[j] == page:
                    used_next = j
                    break

            # if its not used again then we can evict it
            if used_next is None:
                chosen_frame = idx
                farthest_frame = n + 1
                break

            # if not then keep the one used farthest in the future
            if used_next > farthest_frame:
                farthest_frame = used_next
                chosen_frame = idx

        # now exict the chosen frame and add the new request
        frames.pop(chosen_frame)
        frames.append(request)
    return pfs

def main():
    # change filename here to test different files
    # "testfiles/<input_file_name_here>.txt"
    filename = "testfiles/test4.txt"

    k, requests = read_file(filename)
    print(f"FIFO    : {fifo(k,requests)}")
    print(f"LRU     : {lru(k,requests)}")
    print(f"OPTFF   : {optff(k,requests)}")



if __name__ == '__main__':
    main()