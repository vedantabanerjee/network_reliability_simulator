import pytest
import networkx as nx


from network_reliability.graph_generation import(
    generate_erdos_renyi,
    generate_barabasi_albert,
    generate_watts_strogatz
)


def test_er_graph():
    G = generate_erdos_renyi(10, 0.5, seed = 42)
    assert isinstance(G, nx.Graph)
    assert G.number_of_nodes() == 10


@pytest.mark.parametrize("n,m", [(5,2), (10,3)])
def test_ba_graph(n,m):
    G = generate_barabasi_albert(n,m, seed = 123)
    assert G.number_of_nodes() == n
    assert G.number_of_edges() >= n - 1


@pytest.mark.parametrize("n,k,p", [(10,4,0.1), (20,2,0.5)])
def test_ws_graph(n,k,p):
    G = generate_watts_strogatz(n, k, p, seed = 7)
    assert G.number_of_nodes() == n
    assert G.number_of_edges() >= n