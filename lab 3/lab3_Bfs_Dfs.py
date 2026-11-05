from collections import deque

# Graph
graph = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["F"],
    "D":[],
    "E":["G"],
    "F":[],
    "G":[]
}

def bfs(start,goal):
    queue=deque([(start,[start])])
    visited = {start}

    while queue:
        node,path=queue.popleft()

        if node== goal:
            return path

        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                queue.append((child,path+[child]))

def dfs(start,goal):
    stack=[(start, [start])]
    visited= set()

    while stack:
        node,path= stack.pop()

        if node ==goal:
            return path

        if node in visited:
           continue

        visited.add(node)

        for child in reversed(graph[node]):
            stack.append((child,path+[child]))

def bfs_trace(start,goal):
    queue=deque([(start,[start])])
    visited= {start}
    order= []
    step= 0

    print("--- BFS Trace ---")
    while queue:
        node,path= queue.popleft()
        step+=1
        order.append(node)

        print (f"Step   {step}:  Processed    {node}  / Path:   {'->'.join(path)}")

        if node==goal:
            print("Goal reached,remaining queue:",[n for n,p in queue])
            return path,order

        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                queue.append((child,path+[child]))

        print("Queue now:",[n for n,p in queue])

def dfs_trace(start,goal):
    stack= [(start,[start])]
    visited= set()
    order= []
    step= 0

    print("-- DFS Trace --")

    while stack:
        node,path=stack.pop()
        step+=1

        if node==goal:
            order .append  (node)
            print(f"Step {step}:    Processed    {node}  /  Path :    {'->'.join(path)}")
            print  (  "Goal reached,    remaining stack:"   ,   [n for n,p in stack])
            return path,order

        if node in visited:
            print  (f"Step    {step}:     {node} already visited,   skipped")
            continue

        visited.add(node)
        order.append(node)

        print(f"Step {step}:    Processed     {node}    /   Path:     {'->'.join(path)}")

        for child in reversed(graph[node]):
            stack.append((child,path+[child]))

        print  (  "Stack now:",[n for n,p in stack])

if __name__ ==   "__main__":

    print("--- Code Output ---")

    print("BFS:",bfs("A","G"))
    print("DFS:",dfs("A","G"))

    print()

    bfs_path,bfs_order=bfs_trace("A","G")
    print("BFS Final Path:",bfs_path)
    print("BFS Visit Order:",bfs_order)

    print()

    dfs_path,dfs_order=dfs_trace("A","G")
    print("DFS Final Path:",dfs_path)
    print("DFS Visit Order:",dfs_order)

    print()

    print("BFS path matches:",bfs_path==bfs("A", "G"))
    print("DFS path matches:",dfs_path==dfs("A", "G"))

    print("BFS order matches:",
          bfs_order==["A","B","C","D","E","F","G"])

    print("DFS order matches:",
          dfs_order== ["A","B","D","E","G"])