"""
@file testing.py
@author Justin J. Wang <justwjr@ucla.edu>
@date 10/7/16
@brief a .py file of your unit tests, using either nosetests or unittest (nosetest preferred)
"""

from nose.tools import *
from nose import SkipTest

import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

import numpy as np
import networkx as nx

import pprint


# fixture for nose tests
def setup_module(module):
    from nose import SkipTest
    try:
        import numpy
    except:
        raise SkipTest("NumPy not available")
    try:
        import scipy
    except:
        raise SkipTest("SciPy not available")


def test_dangling_node():
    # create 2x2 adjacency matrix, where node B connects to node A, and node A has no out-edges
    # the adjacency matrix would look like:  ('0 0; 0 1')
    # G = nx.Graph()
    G = nx.DiGraph()
    # G.add_edge(2, 1)
    G.add_edge(43521, 9643)

    M = nx.to_numpy_matrix(G)

    # running this test showed me that I had to make a directed graph, because
    logging.debug(M)

    n = len(G)
    p = np.repeat(1.0 / n, n)  # repeat 1/n, n times

    dangling_weights = p

    # dangling nodes are nodes with no out links

    # np.where returns a tuple of arrays where condition is true
    dangling_nodes = np.where(M.sum(axis=1) == 0)
    # dangling_nodes = np.where(M.sum(axis=1) == 0)[0]  # rows that sum to 0
    # dangling_nodes = np.where(M.sum(axis=0) == 0)[0]  # columns that sum to 0

    logging.debug(dangling_nodes)  # we can see that

    # assert_equal(42, 42)
    # assert_not_in('camelCase', inflections)
    # with assert_raises(AttributeError):
    #     object.foo


def test_np_repeat():
    G = nx.DiGraph()
    # G.add_edge(2, 1)
    G.add_edge(43521, 9643)
    # draw_networkx

    n = len(G)
    p = np.repeat(1.0 / n, n)  # repeat 1/n, n times
    logging.debug(p)

    assert_equal(list(p), [.5, .5])

    # nx.draw_networkx(G)


def test_np_array_sum():
    A = np.array([[0, 1, 2, 3],
                  [4, 5, 6, 7],
                  [8, 9, 10, 11]])

    print(A.sum())  # sum all the elements
    print(A.sum(axis=0))  # sum along each column
    print(A.sum(axis=1))  # sum along each row


def test_np_where():
    A = np.array([[0, 1, 2, 3],
                  [4, 5, 6, 7],
                  [8, 9, 10, 11]])

    B = np.array([[0, 1, 0, 3],
                  [0, 5, 0, 7],
                  [0, 9, 0, 11]])

    print(A.sum(axis=1))  # sum along each row

    print(np.where(A.sum(axis=1) == 0)[0])
    # assert (np.where(A.sum(axis=1) == 0)[0] == [])
    # logging.debug(np.where(B.sum(axis=1) == 0)[0])
    pprint.pprint(np.where(B.sum(axis=0) == 0)[0])  # column 0 and 2 sum to 0


# test_dangling_node()
test_np_repeat()
# test_np_array_sum()
# test_np_where()
