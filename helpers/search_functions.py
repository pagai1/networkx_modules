'''
Created on 19.05.2021

@author: pagai
'''
import time
import networkx as nx

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
        print("FINDING NODES WITH DEGREE")
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
    
    if (verbose):
        print(degrees)
        print("NUMBER: " + str(len(degrees)))
    print(time.time() - startTime)
