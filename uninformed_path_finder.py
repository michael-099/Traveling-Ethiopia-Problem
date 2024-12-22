# Implement Depth-First Search (DFS) to find a feasible path to the target city.
# Implement Breadth-First Search (BFS) to find the shortest path based on the number of roads (unweighted).
def uninformed_path_finder_BFS(cities, roads, start_city, goal_city, strategy):
    """
    Parameters:
    - cities: List of city names.
    - roads: Dictionary with city connections as {city: [(connected_city, distance)]}.
    - start_city: The city to start the journey.
    - goal_city: The destination city (for specific tasks).
    - strategy: The uninformed search strategy to use ('bfs' or 'dfs').
    
    Returns:
    - path: List of cities representing the path from start_city to goal_city.
    - cost: Total cost (number of steps or distance) of the path.
    """
    
    def BFS():
        pass
    
    def DFS():
        pass
    
    if strategy=="BFS":
        return BFS()
    else :
        return DFS()
    