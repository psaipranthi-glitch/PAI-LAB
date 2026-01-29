import heapq

def water_jug_astar(cap1, cap2, target):
    
    h = lambda a, b: abs(a - target) + abs(b - target)

    pq = [(h(0, 0), 0, 0, 0, [(0, 0)])]  
    visited = set()

    while pq:
        f, g, j1, j2, path = heapq.heappop(pq)

        if (j1, j2) in visited:
            continue
        visited.add((j1, j2))

        if j1 == target or j2 == target:
            return path

        
        moves = [
            (cap1, j2), (j1, cap2),    
            (0, j2), (j1, 0),           
            (j1 - min(j1, cap2 - j2), j2 + min(j1, cap2 - j2)), 
            (j1 + min(j2, cap1 - j1), j2 - min(j2, cap1 - j1))   
        ]

        for nj1, nj2 in moves:
            if (nj1, nj2) not in visited:
                heapq.heappush(
                    pq,
                    (g + 1 + h(nj1, nj2), g + 1, nj1, nj2, path + [(nj1, nj2)])
                )

    return None



solution = water_jug_astar(4, 3, 2)
for step in solution:
    print(step)
