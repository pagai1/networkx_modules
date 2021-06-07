'''
Created on 17.05.2021

@author: pagai
'''
import time
import networkx as nx
from algoPackage.helpers import to_ms

def algo_betweenness_centrality(G):
#    actor_list=[x for x,y in G.nodes(data=True) if y['type'] == 'actor']
#    subG = G.subgraph(actor_list)
    dict_nodes = []
    algoTime=time.time()    
    dict_nodes = nx.betweenness_centrality(G,normalized=False, endpoints=False);
    print("RUNTIME BetweennessCentrality - " +  str(len(G.nodes())) + " entries - " + to_ms((time.time() - algoTime)) + "s.")   
    print("Result:")
    for bums in dict(sorted(dict_nodes.items(), key=lambda item: item[1])):
        print(dict_nodes[bums],G.nodes[bums]['name'])
#    print("RUNTIME ClosenessCentrality - " +  str(limit) + " entries - " + str(len(actor_list)) + " actors : " + to_ms((time.time() - algoTime)) + "s.")


