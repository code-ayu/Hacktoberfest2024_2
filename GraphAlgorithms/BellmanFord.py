class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.edges = []  # List of edges

    # Function to add an edge to the graph
    def add_edge(self, u, v, weight):
        self.edges.append([u, v, weight])

    # Bellman-Ford algorithm to find the shortest path from src to all other vertices
    def bellman_ford(self, src):
        # Initialize distances from src to all vertices as infinity and src to itself as 0
        dist = [float("inf")] * self.V
        dist[src] = 0

        # Relax all edges |V| - 1 times
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if dist[u] != float("inf") and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        # Check for negative-weight cycles
        for u, v, weight in self.edges:
            if dist[u] != float("inf") and dist[u] + weight < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # Print the calculated shortest distances
        self.print_solution(dist)

    # Function to print the result
    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

# Example usage
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

# Find shortest paths from vertex 0
g.bellman_ford(0)
