graph={
    'A':['B','D'],
    'B':['A','C'],
    'C':['B'],
    'D':['A','E','H'],
    'E':['D','F'],
    'F':['E'],
    'G':['H'],
    'H':['D','G']
}
vis=[]
q=[]

def bfs(node):
    q.append(node)
    vis.append(node)
    while True:
        m=q.pop(0)
        print(m)
        #n is neighbour
        for n in graph[m]:
            if n not in vis:
                vis.append(n)
                q.append(n)

bfs("A")