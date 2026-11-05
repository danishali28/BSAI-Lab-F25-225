import heapq
from collections import deque

graph={
    "A":[("B",1),("C",5)],
    "B":[("D",2),("E",1)],
    "C":[("F",2),("G",7)],
    "D":[],
    "E":[("G",1)],
    "F":[],
    "G":[]
}

def ucs(start,   goal,g=graph):
    pq = [(0,start,[start])]
    visited= set()
    order =[]

    while pq:
        cost,  node, path=heapq.heappop(pq)

        if node in visited:
         continue

        visited.add  (node)
        order.append  ((node,cost))

        if node ==goal:
            return path,cost,order

        for child, weight in g  [node]:
            if child not in visited:
                heapq.heappush(
                    pq,(cost+weight,child,path+[child])
                )

    return None,None,order

def bfs(start,  goal,g=graph):
    queue= deque([(start,[start])])
    visited ={start}
    order=[]

    while queue:
        node,path=queue.popleft()
        order.append  (node)

        if node==goal:
            return path,order

        for child, weight in g  [node]:
            if child not in visited:
                visited.add (child)
                queue.append ((child, path + [child]))

    return None,order

def path_cost(path,g=graph):
    total=0

    for i in range(len(path)-1):
        for child, weight in g  [path[i]]:
            if child==path[i+1]:
                total+=weight

    return total

if __name__ ==   "__main__":

    print("---- Edge Weights----")

    for node in graph:
        for child,weight in graph  [node]:
            print(f"{node}->{child}={weight}")

    path, cost,order=ucs("A","G")

    print("UCS Path:", "->".join(path),"/ Returned Cost:",cost)
    print("UCS Process Order:",order)

    print ("Independent Path Cost:"  ,path_cost(path))

    weights =[dict(graph[a])[b]   for   a, b  in  zip  (path,path[1:])]
    print  ("Manual Sum:", " + ".join (map(str, weights)),  "=",path_cost(path))

    print("Cost Check:",cost==path_cost(path))

    bfs_path, bfs_order=  bfs("A", "G")

    print("BFS Path:", "->".join  (bfs_path))
    print ("BFS Hops:",len(bfs_path)- 1)
    print ("BFS Cost:",path_cost(bfs_path))
    print ("BFS Visit Order:",bfs_order)

    print("--- Edge Cases --")

    print("Start==Goal:", ucs("A", "A"))

    graph2={**graph,"Z":[]}
    print("Unreachable Z:",ucs("A","Z",graph2)[:2])

    cycle={
        "A":  [("B",1)],
        "B":  [("C",1)],
        "C":  [("A",1), ("D",4)],
        "D":  []
    }

    print("Cycle Graph:",ucs   ("A",  "D", cycle))