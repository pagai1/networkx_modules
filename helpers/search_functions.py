'''
Created on 19.05.2021

@author: pagai
'''
import os
import sys
import time
import networkx as nx
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(__file__),"../../networkx_modules")))
from helpers.generalStuff import *

def find_nodes_by_degree(G,inputDegree,function="eq",verbose=False):
    """
    Finds nodes by given degree.
    Parameters
    ----------
    G : Networkx graph
       A graph
    function : String
        Function can be
        eq = equals (default)
        gt = greater than
        lt = lower than
        ge = greater or equal
        le = lower or equal
    
    inputDegree : int
        The degree to search for.
    
        
    Returns : 
        Consoleoutput
    """
    if (verbose): 
        print("FINDING NODES WITH DEGREE " + function.upper() + " " + str(inputDegree) + ".")
    #nodeList = [x for x,y in G.nodes() if G.nodes[x].degree() == 1]
      
    startTime = time.time()     
    if (function == "eq"):
        degrees = [node for (node,val) in G.degree() if val == inputDegree]
    if (function == "gt"):
        degrees = [node for (node,val) in G.degree() if val > inputDegree]
    if (function == "lt"):
        degrees = [node for (node,val) in G.degree() if val < inputDegree]
    if (function == "ge"):
        degrees = [node for (node,val) in G.degree() if val >= inputDegree]
    if (function == "le"):
        degrees = [node for (node,val) in G.degree() if val <= inputDegree]
    endTime = time.time()
    if (verbose):
        print(degrees)
        print("NUMBER: " + str(len(degrees)))
    print("EXECUTION TOOK: " + to_ms(endTime - startTime) + "ms. FOUND " + str(len(degrees)) + " NODES OUT OF " + str(G.number_of_nodes()) + " NODES.")

