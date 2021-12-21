def TWOsum(a):
    output = []
    done = 0
    for q in range(0,len(a)):
        if done == 1:
            break
        for p in range(0,q):
            if done == 1:
                break
            if a[p] == -a[q] and p !=q:
                output.append(p+1)
                output.append(q+1)
                done = 1
                break
    if len(output) ==0:
        output.append(-1)
        return output
    else:
        return output

def makelist(arr,start,end):
    z = []
    for i in range(start,end):
        z.append(arr[i])
    return z 
a = [] 
file = open("rosalind_2sum.txt","r")
#file = open("2sumTest.txt","r")
list = []
input = []
for line in file:
    list += line.split()
for i in range(0,len(list)):
    input.append(int(list[i]))
totalList = input[0]
size = input[1]
listcount = 0 # checks how many lists we have
check = 0 # checks size of list is fine
index = 2 #list data starts at
i = 1
while(check != size and totalList != listcount ):
    a.append(makelist(input,index,(size)*i+2))
    i +=1
    index += size
    check+=1
    listcount+=1
f = open("2SumOut.txt","w")
for i in range(0,len(a)):
    z = TWOsum(a[i])
    for j in range(0,len(z)):
        f.write(str(z[j])+" ")
    f.write("\n")

    

