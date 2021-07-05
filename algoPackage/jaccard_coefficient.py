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


def algo_jaccard_coefficient(G,ebunch=None, verbose=False):
    peng=0
    if (verbose):
        print("STARTING JACCARD COEFFICIENT CALCULATION")
    algoTime=time.time()   
    jaccard_dict = nx.jaccard_coefficient(G, ebunch)
    algoEndTime = time.time()
    print("RUNTIME JACCARD COEFFICIENT - " +  str(G.number_of_nodes()) + " NODES - " + str(G.number_of_edges()) + " EDGES - " + to_ms((algoEndTime - algoTime)) + "s.")   
    #print(simDict)
    if (verbose):
        for bums in jaccard_dict:
            peng+=1
            print(bums)
    print(peng)
