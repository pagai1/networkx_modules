'''
Created on 19.05.2021

@author: pagai
'''
import json
import networkx as nx
from networkx.readwrite import json_graph

#### NODELINKDATA
def import_node_link_data_to_graph(inputfile):
    print("Importing Node Link Data")
    file_to_read = open(inputfile, 'r')
    json_data = json.loads(file_to_read.read())    
    return json_graph.node_link_graph(json_data, directed=True, multigraph=False)

def export_graph_to_node_link_data(G, outputfile, verbose):
    if (verbose) :
        print("Exporting graph to node_link_data-file")
    file_to_write = open(outputfile, 'w')
    file_to_write.write(json.dumps(json_graph.node_link_data(G)))
#### NODELINKDATA

#### GRAPHML
def export_graph_to_graphML_data(G,outputfile):
    print("Exporting to graphML")
    nx.write_graphml(G, outputfile, prettyprint=True )

def import_graphML_to_graph(inputfile):
    print("Importing graphML file")
    return nx.read_graphml(inputfile)
#### GRAPHML

#### ADJLIST
def export_graph_to_adjlist_data(G,outputfile):
    print("Exporting graph to normal Adj List")
    nx.write_adjlist(G, outputfile, delimiter=',')

def import_adjlist_to_graph(inputfile):
    print("Importing normal Adj List")
    return nx.read_adjlist(inputfile, delimiter=',')
#### ADJLIST

#### MULTILINE ADJLIST
def export_graph_to_multiline_adjlist_data(G,outputfile):
    print("Exporting graph to Multiline Adj List")
    nx.write_multiline_adjlist(G, outputfile, delimiter=',')

def import_multiline_adjlist_to_graph(inputfile):
    print("Importing Multiline Adj List")
    G = nx.read_multiline_adjlist(inputfile,delimiter=',',create_using=nx.DiGraph)
    return G
#### MULTILINE ADJLIST

#### YAML
def export_graph_to_yaml_data(G,outputfile):
    print("Exporting graph to YAML")
    nx.write_yaml(G, outputfile)

def import_yaml_to_graph(inputfile):
    print("Importing YAML")
    G = nx.read_yaml(inputfile)
    return G
#### YAML

#### GML
def export_graph_to_gml_data(G,outputfile):
    print("Exporting graph to GML")
    nx.write_gml(G, outputfile)

def import_gml_to_graph(inputfile):
    print("Importing GML")
    G = nx.read_gml(inputfile)
    return G
#### GML