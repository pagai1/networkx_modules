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

def algo_simRank(G, sourceNode=None, targetNode=None,verbose=False,max_iterations=100):
    if (verbose):
        print("STARTING SIMRANK")
    algoTime=time.time()   
    simDict = nx.simrank_similarity(G,max_iterations=100)
    algoEndTime = time.time()
    print("RUNTIME SimRank - " +  str(G.number_of_nodes()) + " NODES - " + str(G.number_of_edges()) + " EDGES - " + to_ms((algoEndTime - algoTime)) + "s.")   
    #print(simDict)
    if (verbose):
        output = [[simDict[u][v] for v in sorted(simDict[u])] for u in sorted(simDict)]
        for bums in output:
            print(bums)
    return simDict
