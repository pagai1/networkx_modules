'''
Created on 17.05.2021

@author: pagai
'''
import networkx as nx
import time
from algoPackage.helpers import to_ms

# Algorithms
def get_hits(G):
    result = nx.hits(G,max_iter=20,normalized=False)
    print(result[0])
    print(result[1])    
    

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

