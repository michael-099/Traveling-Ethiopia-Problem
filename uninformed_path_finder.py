# Implement Depth-First Search (DFS) to find a feasible path to the target city.
# Implement Breadth-First Search (BFS) to find the shortest path based on the number of roads (unweighted).

from collections import deque

def uninformed_path_finder(cities, roads, start_city, goal_city, strategy):
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
    def BFS(start_city, roads, goal_city):
        queue = deque([start_city])
        visited = [start_city]
        path = []
        while queue:
            curr = queue.popleft()
            path.append(curr)
            if curr == goal_city:
                print(visited)
                return path
            for neighbor in roads[curr]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        print(visited)
        return path

    def DFS(start_city, goal_city, roads):
        stack = [start_city]
        visited = [start_city]
        path = []
        while stack:
            curr = stack.pop()
            path.append(curr)
            if curr == goal_city:
                print(visited)
                return path
            for neighbor in roads[curr]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    stack.append(neighbor)
        print(visited)
        return path

    if strategy == "BFS":
        return BFS(start_city, roads, goal_city)
    else:
        return DFS(start_city, goal_city, roads)

if __name__ == "__main__":
    cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
    roads = {
        'Addis Ababa': ['Bahir Dar', 'Hawassa'],
        'Bahir Dar': ['Addis Ababa', 'Gondar'],
        'Gondar': ['Bahir Dar', 'Mekelle'],
        'Hawassa': ['Addis Ababa'],
        'Mekelle': ['Gondar']
    }
    print("hello")

    uninformed_path_finder(cities, roads, "Bahir Dar", "Gondar", "BFS")
    uninformed_path_finder(cities, roads, "Bahir Dar", "Gondar", "DFS")
