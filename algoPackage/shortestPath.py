'''
Created on 17.05.2021

@author: pagai
'''

import networkx as nx
import time
from algoPackage.helpers import to_ms


def algo_shortest_path(G, startNode=None, endNode=None, nodeType=None, forceSubGraphCreation=False):
    if ((nodeType != None) & (forceSubGraphCreation)):
        nodeList=[x for x,y in G.nodes(data=True) if y['type'] == nodeType]
        subG = G.subgraph(nodeList)
    else: 
        subG = G
    start_time_single=time.time()
    try:
        path = nx.shortest_path(subG, source=(startNode), target=endNode)
    except nx.NetworkXNoPath as e:
        path = e
    except nx.NodeNotFound as e:
        path = e
    print("RUNTIME ShortestPath: " + str(path) + to_ms(time.time() - start_time_single) + "\n")
    
def all_algo_shortest_path(G,nodeType=None,verbose=False,createSubgraph=False):
    if ((nodeType != None)):
        print("CREATING SUBGRAPH FOR NODETYPE: " + nodeType)
        print(G.nodes(data=True))
        nodeList=[x for x,y in G.nodes(data=True) if y['label'] == nodeType]
        subG = G.subgraph(nodeList)
        print(subG.nodes())
    else:
        subG = G
        nodeList=subG.nodes()
    print("########################")
    print(G.edges())    
    for edge in G.edges():
        print(G.get_edge_data(edge[0],edge[1]))
    print("Example: Calculating shortest path from anyone to anyone")
    start_time=time.time()
#    for startNode in subG.nodes():
#        for endNode in subG.nodes():
#            if startNode != endNode:
#                start_time_single = time.time() 
#                try:
#                    path = nx.shortest_path(subG, source=(startNode), target=endNode)
#                except nx.NetworkXNoPath as e:
#                    path = e
#                except nx.NodeNotFound as e:
#                    path = e
#                print("PATH: " + str(path) + " - "+ to_ms(time.time() - start_time_single) + " s")    
    #     print(path)
    end_time=time.time()
    print("RUNTIME ShortestPath: " + str(end_time - start_time) )