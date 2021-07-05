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

def algo_pagerank(G, weightInput, functionType, verbose, idDict=None):
    start_time_all = time.time()
    if (weightInput != None):
        start_time = time.time()
        calculation = nx.pagerank(G, alpha=0.85, max_iter=100, weight=weightInput)
        print("TIME: " + to_ms(time.time() - start_time) + " s.")
    else:
        if (functionType == "default"):
            start_time = time.time()
            calculation = nx.pagerank(G, alpha=0.85, max_iter=100)
            print("TIME " + functionType + "   : "+ to_ms(time.time() - start_time) + " s.")
        if (functionType == "numpy"):
            start_time = time.time()
            calculation = nx.pagerank_numpy(G, alpha=0.85)
            print("TIME " + functionType + "   : "+ to_ms(time.time() - start_time) + " s.")
        if (functionType == "scipy"):
            start_time = time.time()
            calculation = nx.pagerank_scipy(G, alpha=0.85, max_iter=100)
            print("TIME " + functionType + " : "+ to_ms(time.time() - start_time) + " s.")
    if (verbose):
        print("Result:")
        i=0
        #print(calculation)
        for node in sorted(calculation.items(), key=lambda item: item[1], reverse=True):
            #value=[y for x,y in dict(sorted(calculation.items(), key=lambda item: item[1], reverse=True)) if x == node]
            print(node)
            #print(str([x for x,y in idDict.items() if y == node[0]]) + " SCORE: " + str(node))
            #print(str(G.nodes()[node[0]]) + " DEGREE: " + str(G.degree(node[0])))
            #print(str(G.nodes(node)) + " --- " + str(dict(sorted(calculation.get(node)))))
            i += 1
            if i > 25:
                break
        print("RUNTIME PageRank: ", time.time() - start_time_all)