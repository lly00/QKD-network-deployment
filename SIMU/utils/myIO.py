import csv
import networkx as nx
import re



def read_file(filename,begin = 0):
        if re.match(r'.*\.csv',filename):
            return read_csv(filename,begin)

def read_csv(filename,begin):
        G = nx.Graph()
        with open(filename) as f:
            data = csv.reader(f)
            G.add_weighted_edges_from(list(data)[begin:])
            return G


