"""
Вам дан взвешенный ориентированный граф, содержащий n вершин и m рёбер.
Найдите минимально возможную сумму весов n−1 ребра, которые нужно оставить в графе,
чтобы из вершины с номером 1 по этим ребрам можно было добраться до любой другой вершины.
______________
TEST1
input:
2 1
2 1 10

output:
NO
_______________
TEST2
input:
4 5
1 2 2
1 3 3
1 4 3
2 3 2
2 4 2

output:
YES
6
"""

import math
from collections import defaultdict
from itertools import chain


def coalesce(value, default_value):
    return value if value is not None else default_value


class Edge:
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight


class OrderedGraph:
    DEFAULT_COLOR = 0

    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = defaultdict(list)

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(Edge(from_node, to_node, weight))

    def build_reverse(self):
        reversed_graph = OrderedGraph(self.nodes)
        for edge in chain.from_iterable(self.edges.values()):
            reversed_graph.add_edge(edge.to_node, edge.from_node, edge.weight)
        return reversed_graph

    def _dfs_components(self, node, colors, counter):
        colors[node] = counter
        for edge in self.edges[node]:
            if colors[edge.to_node] == OrderedGraph.DEFAULT_COLOR:
                self._dfs_components(edge.to_node, colors, counter)

    def components(self, ordered_nodes):
        colors = defaultdict(lambda: OrderedGraph.DEFAULT_COLOR)
        components = 0
        for node in ordered_nodes:
            if colors[node] == OrderedGraph.DEFAULT_COLOR:
                components += 1
                self._dfs_components(node, colors, components)
        return components, colors

    def _dfs_topology(self, node, used, tout, time):
        used.add(node)
        for edge in self.edges[node]:
            if edge.to_node not in used:
                time = self._dfs_topology(edge.to_node, used, tout, time)
        tout[node] = time
        time += 1
        return time

    def _unsafe_topology(self):
        time_out = defaultdict(lambda: 0)
        used = set()
        time = 0
        for node in list(self.edges.keys()):
            if node not in used:
                time = self._dfs_topology(node, used, time_out, time)
        return sorted(range(1, self.nodes + 1), key=time_out.__getitem__, reverse=True)

    def _condensate_wo_edges(self):
        pseudo_topology_sort = self._unsafe_topology()
        components, node_to_component = self.build_reverse().components(pseudo_topology_sort)
        cond_graph = OrderedGraph(components)
        return cond_graph, node_to_component

    def get_node_component(self, node, used=None):
        used = coalesce(used, set())
        used.add(node)
        for edge in self.edges[node]:
            if edge.to_node not in used:
                used = self.get_node_component(edge.to_node, used)
        return used

    def find_mst(self, start_node):
        graph = self
        mst_weight = 0
        while True:
            if len(graph.get_node_component(start_node)) != graph.nodes:
                return False, mst_weight

            min_weights = [math.inf for _ in range(graph.nodes)]
            for edge in chain.from_iterable(graph.edges.values()):
                min_weights[edge.to_node - 1] = min(edge.weight, min_weights[edge.to_node - 1])

            for node in range(1, graph.nodes + 1):
                if node == start_node:
                    continue
                mst_weight += min_weights[node - 1] if min_weights[node - 1] != math.inf else 0

            zero_edges_graph = OrderedGraph(graph.nodes)
            for edge in chain.from_iterable(graph.edges.values()):
                if edge.weight == min_weights[edge.to_node - 1]:
                    zero_edges_graph.add_edge(edge.from_node, edge.to_node, 0)
            if len(zero_edges_graph.get_node_component(start_node)) == graph.nodes:
                return True, mst_weight

            condensate, node_to_comp = zero_edges_graph._condensate_wo_edges()
            for edge in chain.from_iterable(graph.edges.values()):
                if node_to_comp[edge.from_node] != node_to_comp[edge.to_node]:
                    condensate.add_edge(node_to_comp[edge.from_node], node_to_comp[edge.to_node],
                                        edge.weight - min_weights[edge.to_node - 1])
            start_node = node_to_comp[start_node]
            graph = condensate


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    graph = OrderedGraph(n)
    for _ in range(m):
        a, b, w = list(map(int, input().split()))
        graph.add_edge(a, b, w)
    can_build_mst, weight = graph.find_mst(1)
    if can_build_mst:
        print('YES')
        print(weight)
    else:
        print('NO')

