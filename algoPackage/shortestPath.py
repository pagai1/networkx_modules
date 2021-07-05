'''
Created on 17.05.2021

@author: pagai
'''

import networkx as nx
import time
# import own helper-modules
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(__file__),"../../networkx_modules")))
from helpers.generalStuff import *


def algo_all_pairs_bellman_ford_path(G, inputWeight=None, verbose=False):
    print("CALCULATING ALL PAIRS SHORTEST PATHS WITH BELLMAN FORD...")
    start_time = time.time()
    pathdict = dict(nx.all_pairs_bellman_ford_path(G, inputWeight))
    print("CALCULATED PATHDICT IN : " + to_ms(time.time() - start_time))
    if (verbose):
        for key in pathdict.keys():
            print(pathdict[key])
            break
    

def algo_all_pairs_dijkstra(G, inputCutoff=None, inputWeight=None,verbose=False):
    print("CALCULATING ALL PAIRS SHORTEST PATHS WITH DIJKSTRA...")
    start_time = time.time()
    #for n, (dist, path) in nx.all_pairs_dijkstra(G):
    #    print(path[3])
    pathdict = dict(nx.all_pairs_dijkstra(G, cutoff=inputCutoff, weight=inputWeight))
    print("CALCULATED PATHDICT IN : " + to_ms(time.time() - start_time))
    if(verbose):
        for key in pathdict.keys():
            print("SHOWING SINGLE NODE: " + str(pathdict[key]))
            break
        print("SHOW SINGLE PATHS")
        try:
            for p in nx.all_shortest_paths(G, '1','110',weight='weight',method='dijkstra'):
                print(p)
        except Exception:
            print("No path found. Missing source or target in graph")
        print("#######################")
        for node1 in pathdict.keys():
            for node2 in pathdict.keys():
                try:
                    print(f"{node1} - {node2}: {pathdict[node1][0][node2]}")
                except (KeyError,Exception):
                    print("No shortest path between " + node1 + " and " + node2)
        
    

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


def all_pairs_shortest_path(G,nodeTypeForSubGraph=None,verbose=False,inputWeight=None):
    if (nodeTypeForSubGraph != None):
        if (verbose):
            print("CREATING SUBGRAPH FOR NODETYPE: " + nodeTypeForSubGraph)
            print("Graphdata:")
            print(G.nodes(data=True))
        nodeList=[x for x,y in G.nodes(data=True) if y['label'] == nodeTypeForSubGraph]
        subG = G.subgraph(nodeList)
    else:
        subG = G
    if (verbose):
        print("Example: Calculating shortest path from anyone to anyone")
    start_time=time.time()
    paths = nx.shortest_path(subG, weight=inputWeight)
    for path in paths:
        print(path)
    print("RUNTIME ShortestPath: " + to_ms(time.time() - start_time) )


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