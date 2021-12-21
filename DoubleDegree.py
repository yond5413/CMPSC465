def doubleDegree(arr,nodes,edges):
    out = []
    for i in range(0,nodes):
        out.append(0)
    degrees = degree(arr,nodes)
    
    for i in range(0,edges*2,2):    
        node1 = arr[i]
        node2 = arr[i+1]
        out[node1-1] += degrees[node2-1]
        out[node2-1] += degrees[node1-1]
    return out
def degree(arr,nodes):
    out = []
    for i in range(0,nodes):
        out.append(0)
    for i in range(0,len(arr)):
        out[arr[i]-1] +=1
    return out
file = open("rosalind_ddeg.txt","r")
#file = open("DoubleTest.txt","r")
list = []
input = []
for line in file:
    list += line.split()
for i in range(0,len(list)):
    input.append(int(list[i]))
nodes = input[0]
edges = input[1]
a = []
for i in range(2,len(input)):
    a.append(input[i])
f = open("DoubleOut.txt","w")
z = doubleDegree(a,nodes,edges)
for i in range(0,len(z)):
    f.write(str(z[i])+" ")