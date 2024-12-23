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
    
    def BFS(start_city,roads,goal_city):
        queue=deque()
        queue.append(start_city)
        visited=[start_city]
        arr=[]
        while queue:
            curr=queue.popleft()
            print(curr)
            arr.append(curr)
            for i in range(len(roads[curr])):
                if roads[curr][i]==goal_city:
                    visited.append(roads[curr][i])
                    print(visited)
                    return
                if roads[curr][i]not in visited:
                    visited.append(roads[curr][i])
                    queue.append(roads[curr][i])        
        print(visited)
        
    
    def DFS(start_city,goal_city,roads):
        stack=[]
        
            
            
        
        
        
    
    
    if strategy=="BFS":
       BFS(start_city,roads,goal_city)
    else :
        DFS()


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

    uninformed_path_finder(cities,roads,"Bahir Dar","Gondar","BFS")
