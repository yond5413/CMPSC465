def read_pair(fh):
    line = fh.readline()
    line = line.split()
    return (int(line[0]),int(line[1]))

def dfs(adj, mark, u, order):
    mark[u] = True
    for v in adj[u]:
        if mark[v] == False:
            dfs(adj,mark,v,order)
    order.append(u)

#fh = open("top_sortTest.txt")
fh = open("rosalind_ts.txt")
n,m = read_pair(fh)
adj = [[] for u in range(n)]
for e in range(m):
    u, v = read_pair(fh)
    adj[u-1].append(v-1)
order = []
mark = [False] * n 
for u in range(n):
    if mark[u] == False:
        dfs(adj,mark,u,order)

order.reverse()
for i in order:
    print(str(i+1)," ")
