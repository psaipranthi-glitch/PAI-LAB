import heapq

def water_jug_astar(cap1, cap2, target):
    # heuristic: distance from target
    h = lambda a, b: abs(a - target) + abs(b - target)

    pq = [(h(0, 0), 0, 0, 0, [(0, 0)])]  # (f, g, jug1, jug2, path)
    visited = set()

    while pq:
        f, g, j1, j2, path = heapq.heappop(pq)

        if (j1, j2) in visited:
            continue
        visited.add((j1, j2))

        if j1 == target or j2 == target:
            return path

        # all possible moves
        moves = [
            (cap1, j2), (j1, cap2),     # fill
            (0, j2), (j1, 0),           # empty
            (j1 - min(j1, cap2 - j2), j2 + min(j1, cap2 - j2)),  # pour 1→2
            (j1 + min(j2, cap1 - j1), j2 - min(j2, cap1 - j1))   # pour 2→1
        ]

        for nj1, nj2 in moves:
            if (nj1, nj2) not in visited:
                heapq.heappush(
                    pq,
                    (g + 1 + h(nj1, nj2), g + 1, nj1, nj2, path + [(nj1, nj2)])
                )

    return None


# Example
solution = water_jug_astar(4, 3, 2)
for step in solution:
    print(step)
