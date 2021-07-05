'''
Created on 17.05.2021

@author: pagai
'''
import networkx as nx
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.realpath(__file__),"../../networkx_modules")))
from helpers.generalStuff import *
from helpers.networkx_load_n_save import *

# Algorithms
def get_hits(G):
    result = nx.hits(G,max_iter=100,normalized=False)
    count=0
    for bums in result:
        count=0
        for peng in dict(sorted(bums.items(),key=lambda item: item[1], reverse=True)):
            if (count < 25):
                print(peng, bums[peng])
                count = count + 1
        print("=================")
            
    
    
    #print(result[0])
    #print(result[1])    
    

#def get_hits(G):
#    hubs_auths = {}
#    algoTime=time.time() 
#    peng = nx.hits(G,max_iter=20,normalized=True)
#    print("RUNTIME Hits - " +  str(len(G.nodes())) + " entries - " + to_ms((time.time() - algoTime)) + "s.")   
#    for dings in peng:
#        for bums in dict(sorted(dings.items(),key=lambda item: item[1])):
#            print(bums,dings[bums],G.nodes[bums]['name'])
##    for bums in nx.hits(G,max_iter=500,normalized=True):
##        for bla in bums:
##            print(str(bla))

