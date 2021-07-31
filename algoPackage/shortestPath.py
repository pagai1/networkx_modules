'''
Created on 17.05.2021

@author: pagai
'''

import networkx as nx
import time
# import own helper-modules
import sys
import os
import math
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(__file__),"../../networkx_modules")))
from helpers.generalStuff import *

def algo_shortest_path_astar(G, source, target, verbose=True):
    # Calculates the hypothenuse between 2 points in the coordinate system
    def heuristic_distance(s,t):
        sx = float(G.nodes[s]['x'])
        sy = float(G.nodes[s]['y'])
        tx = float(G.nodes[t]['x'])
        ty = float(G.nodes[t]['y'])
        # Hypothenuse multiplied by 10000 to have a better weight in calculation. x.y < xxxx.y    
        result = (math.sqrt(abs(sx-tx)**2 + abs(sy-ty) ** 2) * 10000) 
        return result
    
    start_time=time.time()    
    plz_list=nx.astar_path(G, str(source) , str(target), heuristic=heuristic_distance, weight="weight")

    if (verbose):
        print("RUNTIME SHORTESTPATH WITH ASTAR WAS : " + to_ms(time.time() - start_time) + " ms")
        for bums in plz_list:
            print(G.nodes(data=True)[bums]['name'])

def algo_all_pairs_shortest_path_astar(G,verbose=False):
    start_time=time.time()
    nodeList = G.nodes()
    for source in nodeList:
        for target in nodeList:
            if source != target:
                algo_shortest_path_astar(G, source, target, verbose=verbose)
    end_time = time.time()
    print("RUNTIME allPairsShortestPath aStar (Nodes,Edges,Runtime): " + str(G.number_of_nodes()) + "," + str(G.number_of_edges()) + "," + to_ms(end_time - start_time))
        
def algo_all_pairs_bellman_ford_path(G, inputWeight=None, verbose=False):
    print("CALCULATING ALL PAIRS SHORTEST PATHS WITH BELLMAN FORD...")
    start_time = time.time()
    pathdict = dict(nx.all_pairs_bellman_ford_path(G, inputWeight))
    print("CALCULATED PATHDICT IN : " + to_ms(time.time() - start_time))
    if (verbose):
        for key in pathdict.keys():
            print(pathdict[key])
            break


def algo_all_pairs_dijkstra(G, inputCutoff=None, inputWeight=None, verbose=False):
    if (verbose): 
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
        nodeList=[x for x,y in G.nodes(data=True) if y['labels'] == nodeType]
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


def algo_all_pairs_shortest_path(G,nodeTypeForSubGraph=None,verbose=False,inputWeight=None):
    if (nodeTypeForSubGraph != None):
        if (verbose):
            print("CREATING SUBGRAPH FOR NODETYPE: " + nodeTypeForSubGraph)
            print("Graphdata:")
            print(G.nodes(data=True))
        nodeList=[x for x,y in G.nodes(data=True) if y['labels'] == nodeTypeForSubGraph]
        subG = G.subgraph(nodeList)
    else:
        subG = G
    if (verbose):
        print("Calculating shortest path from anyone to anyone")
    nodeList = G.nodes()
    start_time=time.time()
    paths = nx.shortest_path(subG, weight=inputWeight)
    endTime_path = (time.time()-start_time)
    start_time=time.time()
    for source in nodeList:
        for target in nodeList:
            try:
                pathLength=nx.shortest_path_length(G, source, target, inputWeight)
                if (verbose): 
                    print(str(paths[source][target]) + " " +str(nx.shortest_path_length(G, source, target, inputWeight,method="bellman-ford")))
            except (KeyError,Exception):
                if (verbose):
                    print("No shortest path between " + source + " and " + target)   
    end_time=time.time()
    print("RUNTIME allPairsShortestPath: " + str(subG.number_of_nodes()) + "," + str(subG.number_of_edges()) + "," + to_ms(endTime_path) + "," + to_ms(end_time - start_time) )

def all_algo_shortest_path(G,nodeType=None,verbose=False,createSubgraph=False):
    if ((nodeType != None)):
        print("CREATING SUBGRAPH FOR NODETYPE: " + nodeType)
        print(G.nodes(data=True))
        nodeList=[x for x,y in G.nodes(data=True) if y['labels'] == nodeType]
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