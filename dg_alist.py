class Edge:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst


class Graph:
    def __init__(self, edges, N):
        self.adj = [[]for _ in range(N)]
        for cur in edges:
            self.adj[cur.src].append(cur.dst)

def print_graph(graph):
    for src in range(len(graph.adj)):
        for dst in graph.adj[src]:
            print(f'({src} -> {dst})', end = '')
        print()


if __name__ == '__main__':
    edges = [Edge(0, 1), Edge(1, 2), Edge(2, 0), Edge(2, 1), Edge(3, 2),
             Edge(4, 5), Edge(5, 4)]
    N = 6
    graph = Graph(edges, N)
    print_graph(graph)