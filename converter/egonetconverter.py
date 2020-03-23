import networkx as nx
import os
import pickle
from math import ceil, log10


def write_graph_list(name, graph_list, data_root):
    """Given a list of graphs in networkx format, write each of them
    in its own little gml file in a folder named name in the data_root folder.
    Create the folder, if necessary."""

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
                return '    label "1"\n'

        fixed_lines = map(sanitize_labels, lines)

        f = open(os.path.join(data_path, f'{i:0{format_positions}d}.gml'), 'w')
        f.writelines(fixed_lines)
        f.close()


def write_label_list(name, label_list, data_root):
    """Create a Label.txt file in the folder named name from the labels that are provided."""

    data_path = os.path.join(data_root, name)
    f = open(os.path.join(data_path, 'Labels.txt'), 'w')
    for l in label_list:
        f.write(str(l) + '\n')
    f.close()


def join_graphs(name, source_folder):
    """Find and combine all graphs of the same size (specified by name) from the different
    original large graphs.
    Create a list of these graphs and a label list, where the label of a graph corresponds to the
    dataset that it is initially from.
    That is, our task will be to predict from which original graph some ego net originates."""
    datasets = filter(lambda x: x.find(name) != -1, os.listdir(source_folder))
    graph_list = list()
    label_list = list()
    for i,d in enumerate(datasets):
        with open(os.path.join(source_folder, d), "rb") as f:
            gnx_list = pickle.load(f)
        graph_list.extend(gnx_list)
        label_list.extend([i] * len(gnx_list))

    return graph_list, label_list


def main(name, source_folder, output_folder):
    graph_list, label_list = join_graphs(name=name, source_folder=source_folder)
    write_graph_list(name, graph_list, data_root=output_folder)
    write_label_list(name, label_list, data_root=output_folder)

if __name__ == '__main__':
    source = '../data/egonets'
    output = '../data'

    main(name='s60to80', source_folder=source, output_folder=output)
    main(name='s80to100', source_folder=source, output_folder=output)
    main(name='s160to180', source_folder=source, output_folder=output)
    main(name='s200to220', source_folder=source, output_folder=output)
    main(name='s200to250', source_folder=source, output_folder=output)
    main(name='s240to260', source_folder=source, output_folder=output)