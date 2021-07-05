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


def algo_degree_centrality(G, verbose=False):
    peng=0
    if (verbose):
        print("STARTING DEGREE CENTRALITY CALCULATION")
    algoTime=time.time()
    degree_centrality = dict(sorted(nx.degree_centrality(G).items(), key=lambda item: item[1]))
    algoEndTime = time.time()
    #print("RUNTIME DEGREE CENTRALITY CALCULATION - " +  str(G.number_of_nodes()) + " NODES - " + str(G.number_of_edges()) + " EDGES - " + to_ms((algoEndTime - algoTime)) + "s.")
    print(str(G.number_of_nodes()) + "," + str(G.number_of_edges()) + "," +  to_ms((algoEndTime - algoTime)))   
    if (verbose):
        for bums in dict(sorted(degree_centrality.items(), key=lambda item: item[1])):
            print(degree_centrality[bums],G.nodes[bums]['name'])
            #print(str(bums) + " - " + str(degree_centrality[bums]))
    