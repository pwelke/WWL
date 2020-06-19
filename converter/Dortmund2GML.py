import sys

import GraphDataToGraphList as d2l
import egonetconverter
import networkx as nx
import os
from math import log10, ceil
import re

def write_graph_list(name, graph_list, data_root):
    """Given a list of graphs in networkx format, write each of them
    in its own little gml file in a folder named name in the data_root folder.
    Create the folder, if necessary.

    This function is very hacky, parsing node labels on the go for datasets obtained from the Dortmund collection at
    https://ls11-www.cs.tu-dortmund.de/staff/morris/graphkerneldatasets
    to allow writing node labeled graphs in the format expected by BorgwardtLab projects WWL and P-WL."""

    data_path = os.path.join(data_root, name)
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    # compute right number of trailing zeros for file names
    format_positions = ceil(log10(len(graph_list)))

    for i, g in enumerate(graph_list):
        lines = nx.generate_gml(g)

        # stupid networkx requires labels to be equal to node ids.
        # we need to fix this
        def sanitize_labels(x):
            if x.find('label') == -1:
                return x + '\n'
            else:
                v = x[10:]
                label = g.node[int(v)]['label']
                return f'    label "{label}"\n'

        fixed_lines = map(sanitize_labels, lines)

        f = open(os.path.join(data_path, f'{i:0{format_positions}d}.gml'), 'w')
        f.writelines(fixed_lines)
        f.close()

def getLabel(objectData):
    if 'label' in objectData:
        # if there is label data, then the label data is a numpy array with values
        # here, we just return the first value as string
        return str(int(objectData['label'][0]))
    else:
        return '0'

def dumpLabel(g):
    """Very very hacky. Works for BZR and DHFR to remove attributes and make labels compliant."""
    for v in g.nodes():
        g.node[v]['label'] = getLabel(g.node[v])
        del g.node[v]['attribute']

def load_graphs(db, path):
    graphStuff = d2l.graph_data_to_graph_list(path, db)
    graphs = graphStuff[0]
    labels = graphStuff[1]
    indices = range(len(graphs))
    return graphs, labels

if __name__ == '__main__':
    """Convert some graphs from the Dortmund graph kernel benchmark collection to 
    gml format and accompanying label file that is expected by BorgwardtLabs WWL and P-WL projects.
    """

    inpath = sys.argv[1]
    outpath = sys.argv[2]
    db = sys.argv[3]

    G, y = load_graphs(path=inpath, db=db)

    for g in G:
        dumpLabel(g)

    write_graph_list(name=db, graph_list=G, data_root=outpath)
    egonetconverter.write_label_list(name=db, label_list=y, data_root=outpath)
