'''
Created on 19.05.2021

@author: pagai
'''
import json
import csv
import networkx as nx
from networkx.readwrite import json_graph

def create_graph_from_neo4j_csv(filePath, inputDirectedData=True, outputDirectedGraph=True):
    if (outputDirectedGraph):
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    with open(filePath,'r') as csv_file:
        reader = csv.DictReader(csv_file,quotechar = '"', delimiter=',')
        headerfields = list(reader.fieldnames)
        index_first_node_attribute = 1
        index_last_node_attribute = (headerfields.index("_start", 1) - 1)
        index_first_edge_attribute = (headerfields.index("_end", (index_last_node_attribute + 2)) + 1)
        index_last_edge_attribute = (len(headerfields) - 1)
        nodeAttributes = {}
        edgeAttributes = {}
        for line in reader:
            if line['_id'] != "":
                for i in range(index_first_node_attribute, index_last_node_attribute):
                    nodeAttributes[headerfields[i]] = line[headerfields[i]].replace(":","")
                G.add_nodes_from([(line['_id'], nodeAttributes)])
            if line['_start'] != "":
                for i in range(index_first_edge_attribute, index_last_edge_attribute):
                    edgeAttributes[headerfields[i]] = line[headerfields[i]].replace(":","")
                G.add_edges_from([(line['_start'],line['_end'], edgeAttributes)])
                # Wenn die inputDaten nicht gerichtet sind aber der Graph gerichtet sein soll, dann noch eine zweite Kante hinzufügen in Rückrichtung.
                # Wenn inputDaten hingegegen gerichtet sind, dann wird die Rückrichtung noch als Kante kommen und dann hinzugefügt werden.
                # Das passiert aber auch nur, wenn der output als gerichtet gewünscht ist. Ansonsten ist G ja mit nx.Graph() erstellt worden
                # und dann braucht es die Rückrichtung ja überhaupt nicht.
                if not inputDirectedData and outputDirectedGraph:
                    G.add_edges_from([(line['_end'],line['_start'], edgeAttributes)])
                #G.add_edge(line['_start'],line['_end'],type=line['_type'],cost=float(line['cost']),count=int(line['count']),dice=line['dice'])
                #G.add_edge(line['_end'],line['_start'],type=line['_type'],cost=float(line['cost']),count=int(line['count']),dice=line['dice']) 
    return G
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