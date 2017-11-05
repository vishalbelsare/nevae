import os
import pickle
import numpy as np
import networkx as nx
import tensorflow as tf
from numpy.linalg import svd, qr

def degree(A):
    return np.zeros()


def construct_feed_dict(k,i,lr,dropout, placeholders):
    # construct feed dictionary
    feed_dict = dict()
    #feed_dict.update({placeholders['features']: features})
    #feed_dict.update({placeholders['adj']: adj_normalized})
    feed_dict.update({placeholders['k']: k})
    feed_dict.update({placeholders['i']: i})
    feed_dict.update({placeholders['lr']: lr})
    feed_dict.update({placeholders['dropout']: dropout})
    return feed_dict


def get_shape(tensor):
    '''return the shape of tensor as list'''
    return tensor.get_shape().as_list()

def basis(adj, atol=1e-13, rtol=0):
    """Estimate the basis of a matrix.


    Parameters
    ----------
    A : ndarray
        A should be at most 2-D.  A 1-D array with length n will be treated
        as a 2-D with shape (1, n)
    atol : float
        The absolute tolerance for a zero singular value.  Singular values
        smaller than `atol` are considered to be zero.
    rtol : float
        The relative tolerance.  Singular values less than rtol*smax are
        considered to be zero, where smax is the largest singular value.

    If both `atol` and `rtol` are positive, the combined tolerance is the
    maximum of the two; that is::
        tol = max(atol, rtol * smax)
    Singular values smaller than `tol` are considered to be zero.

    Return value
    ------------
    b : ndarray
        The basis of the columnspace of the matrix.

    See also
    --------
    numpy.linalg.matrix_rank
    """

    A = degree(adj) - adj

    A = np.atleast_2d(A)
    s = svd(A, compute_uv=False)
    tol = max(atol, rtol * s[0])
    rank = int((s >= tol).sum())
    q, r = qr(A)
    return q[:rank]

def print_vars(string):
    '''print variables in collection named string'''
    print("Collection name %s"%string)
    print("    "+"\n    ".join(["{} : {}".format(v.name, get_shape(v)) for v in tf.get_collection(string)]))

def get_basis(mat):
    basis = np.zeros(1,1)
    return basis

def create_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
def get_edges(adj):
    G.edges()
    return
def pickle_load(path):
    '''Load the picke data from path'''
    with open(path, 'rb') as f:
        loaded_pickle = pickle.load(f)
    return loaded_pickle
def load_data(filename):
    G=nx.read_edgelist(filename)
    n = G.number_of_nodes() 
    degreemat = np.zeros((n,n), dtype=np.int)
    edges = G.edges()
    GC=nx.complete_graph(n)
    non_edges = list(set(GC.edges()) - set(edges))
    for u in G.nodes():
	degreemat[int(u)][int(u)] = G.degree(u)
    return (tf.convert_to_tensor(nx.adjacency_matrix(G).todense()), tf.convert_to_tensor(degreemat), edges, non_edges)

def pickle_save(content, path):
    '''Save the content on the path'''
    with open(path, 'wb') as f:
        pickle.dump(content, f)
