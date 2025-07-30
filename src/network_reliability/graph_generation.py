
"""
Graph generation utilities for Network Reliability Simulator.
Supported topologies: Erdos-Renyi, Barabasi-Albert and Watts-Strogatz
"""

import networkx as nx


def generate_erdos_renyi(n: int, p:float, seed: int = None) -> nx.Graph:
    """
    Returns an Erdos-Renyi G(n,p) random graph.
    :param n: Number of nodes (must be >=1)
    :param p: Edge Probability in [0,1]
    :param seed: Optional RNG Seed for Reproducibility
    """

    if n < 1:
        raise ValueError("Number of nodes 'n' must be >= 1")
    if not (0.0 <= p <= 1.0):
        raise ValueError("Probability 'p' must be between 0 and 1 (inclusive)")
    return nx.erdos_renyi_graph(n, p, seed = seed)


def generate_barabasi_albert(n: int, m: int, seed: int = None) -> nx.Graph:
    """
    Returns a Barabasi-Albert scale-free graph with n nodes, m edges to attach from a new node.
    :param n: Number of nodes (must be >= m + 1)
    :param m: Edge per new node (>= 1)
    :param seed: Optional RNG Seed for Reproducibility
    """

    if n < m + 1:
        raise ValueError("'n' must be >= m + 1 for a Barabasi-Albert model")
    if m < 1:
        raise ValueError("'m' must be >= 1")
    return nx.barabasi_albert_graph(n, m, seed = seed)


def generate_watts_strogatz(n: int, k:int, p:float, seed:int = None) -> nx.Graph:
    """
    Returns a Watts-Strogatz small-world graph
    :param n: Number of nodes (>= k + 1)
    :param k: Each node is joined with its k nearest neighbours in ring topology (must be even).
    :param p: Rewiring probability in [0,1]
    :param seed: Optional RNG Seed for Reproducibility
    """

    if n < k + 1:
        raise ValueError("'n' must be >= k + 1")
    if k % 2 != 0:
        raise ValueError("'k' must be even")
    if not (0.0 <= p <= 1.0):
        raise ValueError("'p' must be between 0 and 1 (inclusive)")
    return nx.watts_strogatz_graph(n, k, p, seed = seed)