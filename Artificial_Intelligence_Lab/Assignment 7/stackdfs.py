def dfs(maze, start, end):
    stack = [start]  # Initialize stack with the start position
    # This dictionary will store the path like breadcrumbs: {child: parent}
    rev_path = {start: None}
    visited = {start}  # Track visited positions to avoid cycles

    while stack:
        position = stack.pop()  # Get the last added position (LIFO)

        # If we've reached the end, reconstruct and return the path
        if position == end:
            path = []
            while position is not None:
                path.append(position)
                # Correctly access the dictionary using square brackets
                position = rev_path[position]
            return path[::-1]  # Return the reversed path (from start to end)

        x, y = position

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            new_position = (new_x, new_y)

            # Check if the neighbor is valid and unvisited
            if (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and
                    maze[new_x][new_y] == 0 and new_position not in visited):
                
                stack.append(new_position)
                visited.add(new_position)
                # Correctly assign to the dictionary using square brackets
                rev_path[new_position] = position

    return None  # Return None if no path is found

# Example maze: 0 -> open path, 1 -> wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

path = dfs(maze, start, end)

if path:
    print("Path found! ✅")
    print(path)
else:
    print("No path exists. ❌")
