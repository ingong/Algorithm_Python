from collections import deque

# visitable 로 가능한지 체크하는거 좋다
def visitable(n, m, y, x):
    return 0 <= y < n and 0 <= x < m


# 2차원 배열일 경우, 특히 좌표의 특성을 가질 때는 이런식으로 해주는거 굿인듯
# visited
def solution(n, m, image):
    visited, bfs_nodes = set(), deque([])
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    answer = 0

    for y in range(n):
        for x in range(m):
            print(y, x)
            if (y, x) in visited:
                continue
            answer += 1
            bfs_nodes.append((y, x))
            visited.add((y, x))

            while bfs_nodes:
                cur_y, cur_x = bfs_nodes.popleft()
                for dx, dy in deltas:
                    next_y, next_x = cur_y + dy, cur_x + dx
                    if visitable(n, m, next_y, next_x) and (next_y, next_x) not in visited and image[cur_y][cur_x] == image[next_y][next_x]:
                        bfs_nodes.append((next_y, next_x))
                        visited.add((next_y, next_x))

    return answer


result = solution(2, 3, [[1, 2, 3], [3, 2, 1]])
print(result)
