"""
    @file edge_to_graph.py
    @brief This program constructs the adjacency matrix from a list of edges.
    @author Justin J. Wang
    @date 10/8/2016

    https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html
    https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
import networkx as nx
# import scipy as sp

def edges_to_matrix(path):
    """
    This function constructs the adjacency matrix from a list of edges.
    :packages: import networkx as nx
    :param path: text file containing list of edges
    :return: NetworkX graph
    """
    G = nx.DiGraph()

    edge_list = list(open(path))  # list of strings

    for x in edge_list:
        t = tuple(x.replace("\n", "").split("\t"))  # format the string to a tuple
        # print(type(int(t[0])))
        # print(t[0])
        G.add_edge(t[0], t[1])

    # print(G.nodes())
    # print(G.edges())

    # A = nx.adjacency_matrix(G)
    # print(A.todense())

    # A.setdiag(A.diagonal() * 2)  # alternative convention of doubling edge weight
    # print(A.todense())

    return G


# edges_to_matrix("/Users/justin/OneDrive/PageRank/mini_edge_list.txt")
# edges_to_matrix("/Users/justin/OneDrive/PageRank/amazon0302 4.txt")
