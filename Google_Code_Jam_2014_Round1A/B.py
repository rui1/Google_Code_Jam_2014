import re
import time
from sys import stdin

def line():
	return map( int, stdin.readline().strip().split() )
T,= line()
def update(n1,n2, NodeMap):
    if n1 not in NodeMap:
        NodeMap[n1]=set()
    NodeMap[n1].add(n2)

def makeFull(root,or_root,roots,child, NodeMap):
    if root in child or(root != or_root and root in roots):
        return 0
    subs = [x for x in NodeMap[root] if x !=or_root]
    N_nodes = {}
    for sub in subs:
        n_sub=makeFull(sub,root, roots,child,NodeMap)
        N_nodes[sub]=1++n_sub
    return sum(sorted(N_nodes.values(),reverse=True)[:2])

def maxFull(roots,twonodes,leaf, NodeMap):
    best = 3
    for root in roots:
        tmp = 1+makeFull(root, root,twonodes,leaf,NodeMap)
        best = max(tmp,best)
    return best    
        
t1 = time.time()
for t in range(1,T+1):
    N, = line()
    NodeMap = {}
    for n in range(0, N-1):
        n1,n2 = line()
        update(n1,n2, NodeMap)
        update(n2,n1,NodeMap)
    TwoNode = {}
    OneNode = {}
    MultiNode = {}
    for node in NodeMap:
        if len(NodeMap[node])==2:
            TwoNode[node]=NodeMap[node]
        if len(NodeMap[node])==1:
            OneNode[node]=NodeMap[node]
        if len(NodeMap[node])>1:
            MultiNode[node]=NodeMap[node]
    if len(OneNode)==len(NodeMap):
        cuts = 1
    else:
        cuts =N- maxFull(MultiNode,TwoNode, OneNode, NodeMap)
    print 'Case #%d: %d' % (t, cuts)
t2= time.time()
#print t2-t1
    

        
        
