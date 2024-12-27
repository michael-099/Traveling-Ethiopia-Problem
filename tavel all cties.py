from collections import deque
import matplotlib.pyplot as plt
import networkx as nx


def traverse_all_cities(cities, roads, start_city, strategy):
    visited = set()
    path = [start_city]
    cost = 0
    
    if strategy == 'bfs':
        return bfs_traverse_all_cities(cities, roads, start_city)
    elif strategy == 'dfs':
        return dfs_traverse_all_cities(cities, roads, start_city, visited, path, cost)

def bfs_traverse_all_cities(cities, roads, start_city):
    queue = deque([(start_city, [start_city], 0)])  
    visited = set([start_city])
    
    while queue:
        current_city, path, cost = queue.popleft()
        
        for neighbor, distance in roads.get(current_city, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor], cost + distance))
    
    return path, cost

def dfs_traverse_all_cities(cities, roads, current_city, visited, path, cost):
    visited.add(current_city)
    for neighbor, distance in roads.get(current_city, []):
        if neighbor not in visited:
            path.append(neighbor)
            cost += distance
            dfs_traverse_all_cities(cities, roads, neighbor, visited, path, cost)
    return path, cost


cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

path_all, cost_all = traverse_all_cities(cities, roads, 'Addis Ababa', 'bfs')
print(f"Traversal Path: {path_all} with cost {cost_all}")


