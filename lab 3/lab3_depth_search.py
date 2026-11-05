# A starts depth 0 par
graph={
    "A":["B","C"],
    "B":["D","E"],
    "C":["F"],
    "D":[],
    "E":["G"],
    "F":[],
    "G":[]
}

def dls(g,node,goal,limit,path,log):
    log.append(node)

    if node ==goal:
        return "FOUND",path

    if limit== 0:
        for child in g[node]:
            if child not in path:
                return "CUTOFF",None
        return "FAILURE",None

    cutoff=False

    for child in g[node]:
        if child in path:
         continue

        result,new_path=dls(
            g,child,goal,limit-1,
            path+[child],log
        )

        if result== "FOUND":
            return result,new_path

        if result=="CUTOFF":
            cutoff= True

    if cutoff:
        return "CUTOFF",None

    return "FAILURE",None

def run_dls(g,start,goal,limit,log=None):
    if log is None:
        log=[]

    return dls(g,start, goal,limit,[start], log)

def iddfs(g,start,goal,max_depth):
    tried=[]
    result= "FAILURE"

    for limit in range(max_depth +1):
        tried.append  (limit)
        result,path=run_dls (g,start, goal,limit)

        if result ==   "FOUND":
            return result,  path,tried

        if result==   "FAILURE":
            return result,  None,   tried

    return result  , None,   tried

if __name__  ==   "__main__":

    print("=== DLS on Original Graph ====")

    for limit in (1,2,3,4):
        result,path= run_dls(graph,"A","G",limit)
        print(f"Limit={limit}: Status ={result},Path={'->'.join(path) if path else None}")

    print("\n===IDDFS with Maximum Depth 1 to 4   ====")

    for depth in (1,2,3,4):
        result,path,tried=iddfs(graph,"A","G",depth)
        print(f"Max Depth={depth}: Status={result},Path={'->'.join(path) if path else None},Limits Tried= {tried}")

    print("=== Repeated Work in IDDFS ==")

    total =0

    for limit in range(4):
        log=[]
        run_dls(graph,"A","G",limit, log)
        total+=len(log)
        print(f"Limit={limit}:{log}/ Count={len(log)}")

    print("Total Nodes Processed by IDDFS:",total)

    print("===== Edge Cases ======")

    print("Start==Goal:",run_dls(graph,"A","A",0))

    graph2=dict(graph)
    graph2["Z"]=[]

    print("Unreachable Goal Z:")

    for limit in (2,6):
        print(f"DLS Limit={limit}:",run_dls(graph2,"A","Z",limit))

    print("IDDFS Max Depth 6:",iddfs(graph2,"A","Z",6))

    cycle_graph={
        "A":["B"],
        "B":["C"],
        "C":["A","D"],
        "D":[]
    }

    print("Cycle Graph A->B-> C->A,Goal D:")
    print("DLS Limit= 5:",run_dls(cycle_graph,"A","D",5))
    print("IDDFS Max Depth 5:",iddfs(cycle_graph,"A","D",5))

    print("Cycle Graph with Unreachable Goal X:")

    cycle_graph["X"]=[]
    print("DLS Limit=5:", run_dls(cycle_graph,"A", "X",5))