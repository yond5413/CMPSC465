def degree(arr,nodes):
    out = []
    for i in range(0,nodes):
        out.append(0)
    for i in range(0,len(arr)):
        out[arr[i]-1] +=1
    return out
file = open("rosalind_deg.txt","r")
list = []
input = []
for line in file:
    list += line.split()
for i in range(0,len(list)):
    input.append(int(list[i]))
nodes = input[0]
a = []
for i in range(2,len(input)):
    a.append(input[i])
f = open("DegreeOut.txt","w")
z = degree(a,nodes)
for i in range(0,len(z)):
    f.write(str(z[i])+" ")