import heapq
import matplotlib.pyplot as plt

def astar_search(graph, heuristics, start, goal):
    """
    Finds the shortest path from start to goal using the A* algorithm.
    This is an efficient implementation using a priority queue.
    """
    open_set = [(heuristics[start], start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct and return the path if the goal is reached
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristics[neighbor]
                heapq.heappush(open_set, (f_score, neighbor))
    
    return None # Path not found

def visualize_path(graph, heuristics, path, positions, filename="astar_path_visualization.png"):
    """
    Creates and saves a visualization of the graph and the A* path.
    """
    # Create a set of nodes and edges in the path for quick lookups
    path_nodes = set(path)
    path_edges = set(zip(path, path[1:]))

    # Set up the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # --- Draw Edges and their Costs ---
    for node, neighbors in graph.items():
        for neighbor, cost in neighbors.items():
            # Check if the edge is part of the path (in either direction)
            is_path_edge = (node, neighbor) in path_edges or (neighbor, node) in path_edges
            
            line_color = 'green' if is_path_edge else 'lightgray'
            line_width = 3.0 if is_path_edge else 1.0
            
            x1, y1 = positions[node]
            x2, y2 = positions[neighbor]
            
            ax.plot([x1, x2], [y1, y2], color=line_color, linewidth=line_width, zorder=1)
            
            # Add cost labels to edges
            mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
            ax.text(mid_x, mid_y, str(cost), size=12, ha='center', va='center',
                    bbox=dict(facecolor='white', edgecolor='none', pad=0.1))

    # --- Draw Nodes and their Labels ---
    for node, pos in positions.items():
        is_path_node = node in path_nodes
        
        node_color = 'lightgreen' if is_path_node else 'skyblue'
        
        ax.scatter(pos[0], pos[1], s=2500, color=node_color, zorder=2, ec='black')
        # Add node name
        ax.text(pos[0], pos[1], node, ha='center', va='center', fontsize=15, fontweight='bold')
        # Add heuristic value
        ax.text(pos[0], pos[1] - 0.18, f'h={heuristics[node]}', ha='center', va='center', fontsize=12, color='darkred')

    # --- Final Touches ---
    ax.set_title('A* Search Visualization', size=20)
    ax.margins(0.1)
    ax.set_aspect('equal')
    plt.axis('off')
    
    # Save the figure to a file before showing it
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.2)
    print(f"Visualization saved as '{filename}'")
    plt.show()


# =============================================================================
# Main execution block
# =============================================================================
if __name__ == "__main__":
    # 1. Define the graph, heuristics, and node positions
    graph_data = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5, 'D': 12},
    'B': {'C': 2},
    'C': {'D': 3, 'G': 7},
    'D': {'G': 2},
    'G': {}
    }
    heuristic_data = {
    'S': 7, 
    'A': 6, 
    'B': 4,
    'C': 2, 
    'D': 1, 
    'G': 0
    }
    node_positions = {
        'S': (0, 1), 'A': (1, 2), 'B': (1, 0),
        'C': (1.8, .6), 'D': (2, 1.5), 'G': (3, 1)
    }

    # 2. Run the A* algorithm
    start_node, goal_node = 'S', 'G'
    shortest_path = astar_search(graph_data, heuristic_data, start_node, goal_node)
    
    print(f"Shortest path found: {shortest_path}")

    # 3. Visualize the result
    if shortest_path:
        visualize_path(graph_data, heuristic_data, shortest_path, node_positions)
    else:
        print("Could not find a path to visualize.")
