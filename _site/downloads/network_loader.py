import csv
import random
# NOTE: when installing via pip or conda, install python-igraph
from igraph import *

txt_file = 'network_tf_tf_clean.txt'

def open_network(filename) : 
    
    network = Graph(directed=True)
    edge_names = [] 
    vertex_names = []
    num_self_edges = 0 
    
    with open(txt_file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t') 
        # use dictionary and counter to convert gene names to #s
        counter = 0
        gene_dict = {}
        for row in reader :
            # [0] - TF #1, [1] - TF #2, [2] = +,-, +-, ?
            tf1 = row[0].lower()
            tf2 = row[1].lower()
            edge_type = row[2]
            tf1_idx, tf2_idx = 0, 0

            if tf1 not in gene_dict : 
                gene_dict[tf1] = counter
                network.add_vertices(1)
                vertex_names.append(tf1)
                tf1_idx = counter
                counter += 1
            else : 
                tf1_idx = gene_dict[tf1]

            if tf2 not in gene_dict : 
                gene_dict[tf2] = counter
                network.add_vertices(1)
                vertex_names.append(tf2)
                tf2_idx = counter
                counter += 1
            else :
                tf2_idx = gene_dict[tf2]

            if (tf1 == tf2) :
                num_self_edges += 1

            network.add_edge(tf1_idx, tf2_idx)
            edge_names.append(edge_type)
            if (edge_type == '+') :
                network.es[len(edge_names)-1]["color"] = 'green'
            if (edge_type == '-') :
                network.es[len(edge_names)-1]["color"] = 'red'

    return (network, vertex_names)

