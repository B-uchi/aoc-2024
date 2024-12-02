import heapq

with open("input.txt", "r") as f:
    lines = f.readlines()

def first_half():
    sum_diff = 0
    l_heap = []
    r_heap = []

    for line in lines:
        l, r = line.replace("\n", "").split()
        heapq.heappush(l_heap, int(l))
        heapq.heappush(r_heap, int(r))
    for _ in range(len(l_heap)):
        sum_diff += abs(heapq.heappop(l_heap) - heapq.heappop(r_heap))
    return sum_diff

        
def second_half():
    similarity_multiplier = 0
    left = []
    right = []
    
    for line in lines:
        l, r = line.replace("\n", "").split()
        left.append(int(l))
        right.append(int(r))

    for l in left:
        exists = 0
        for r in right:
            if l == r:
                exists += 1
        similarity_multiplier += (l*exists)
 
    return similarity_multiplier


