"""
@file PageRank.py
@author Justin J. Wang <justwjr@ucla.edu>
@date 10/7/16
@brief This program implements the PageRank algorithm, which assigns a rank to a node based on the number of "important"
nodes that link to it.
"""

import edges_to_graph
import networkx as nx
import numpy as np
import pprint
import csv


def page_rank(G, epsilon=.85):
    """
    This algorithm proceeds as follows:
    1. construct A based on the connected structure of the network, where Aij = 1/di if node i connects to node j and di
    is the total number of unique outgoing links from page i
    2. find X s.t. X = e[_1_] + (1-e)*A.T*X, where e is a constant, and [_1_] is a column vector of 1s.  The value X[i]
    is the rank of the ith page.
        # start with a value of X, where each component is 1/n, where n is the number of nodes
        # then, perform the eigenvector solver on the matrix e*[_1_] + (1-e)*A.T
    :param epsilon: the damping factor default initialized to .85
    :param G: matrix representation of a graph of nodes and edges
    :return: dictionary of nodes with PageRank as value
    """

    # construct A based on the connected structure of the network, where Aij = 1/di if node i connects to node j and di
    # is the total number of ! outgoing links from page i
    # A = nx.google_matrix(G)
    # A represents the transition matrix that describes the Markov chain

    M = nx.to_numpy_matrix(G)  # construct adjacency matrix M
    # print("M", M)

    # the personalization vector uses a uniform distribution to create a dictionary with a key for each node and nonzero
    # personalization value for each node.
    n = len(G)
    dangling_weights = np.repeat(1.0 / n, n)  # repeat 1/n, n times

    # dangling nodes are nodes with no out links
    # first return position is array of indices where rows sum to 0

    # assign dangling_weights to any dangling nodes
    dangling_nodes = np.where(M.sum(axis=1) == 0)[0]  # rows that sum to 0
    for x in dangling_nodes:
        M[x] = dangling_weights

    M /= M.sum(axis=1)  # divide each element its column sum, so column sums to 1

    # A represents the transition matrix that describes the Markov chain
    A = epsilon * M + (1 - epsilon) * dangling_weights

    # use numpy linear algebra package eigenvalue/eigenvector solver
    eigenvalues, eigenvectors = np.linalg.eig(A.T)

    # pprint.pprint(eigenvalues)
    # pprint.pprint(eigenvectors)

    # stochastic matrix guarantees that principal eigenvalue is 1
    # sort the indices of the eigenvalues
    indices = eigenvalues.argsort()  # argsort returns the indices of the sorted list

    # normalized eigenvector corresponding to largest eigenvalue at indices[-1]
    largest = np.array(eigenvectors[:, indices[-1]]).flatten().real

    # normalize the largest eigenvector
    return dict(zip(G, map(float, largest / float(largest.sum()))))


def output_results(PI, network_name):
    outputFile = open(network_name + '_results.csv', 'w', newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow(sorted(PI.items(), key=lambda x: x[1], reverse=True))
    outputFile.close()


# print(nx.pagerank(G))
# print(A)
# return ordered list of key, value tuples
# print(sorted(PI.items(), key=lambda x: x[1], reverse=True))
# pprint.pprint(sorted(PI.items(), key=lambda x: x[1], reverse=True))


G = edges_to_graph.edges_to_matrix("../graph network data files/mini_edge_list.txt")
PI = page_rank(G)
output_results(PI, "mini_edge_list")

# amazon = edges_to_graph.edges_to_matrix("../graph network data files/amazon0302 4.txt")
# PI_amazon = page_rank(amazon)
# output_results(PI_amazon, "amazon_purchases")
