from collections import deque

def bfs_find_path(maze, start, end):
    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([start])
    visited = {start}
    
    # This dictionary stores the path: {child_cell: parent_cell}
    came_from = {start: None}

    while queue:
        current = queue.popleft()

        if current == end:
            # Reconstruct the path by working backward from the end
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1],came_from # Return the reversed path (start to end)

        for direction in directions:
            next_cell = (current[0] + direction[0], current[1] + direction[1])

            if (0 <= next_cell[0] < len(maze) and
                    0 <= next_cell[1] < len(maze[0]) and
                    maze[next_cell[0]][next_cell[1]] != '#' and
                    next_cell not in visited):
                
                queue.append(next_cell)
                visited.add(next_cell)
                
                # Record that we came from 'current' to get to 'next_cell'
                came_from[next_cell] = current

    return None  # No path found

# Example maze
maze = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', 'E'],
]

start = (0, 0)
end = (6, 6)

# Run BFS to find the path
path = bfs_find_path(maze, start, end)

if path:
    print("Path found! ✅")
    print(path)
else:
    print("No path exists. ❌")
