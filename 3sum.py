def Threesum(arr):
    output = []
    for p in range(0,len(arr)-2):#0<= p<q<r<=n
        q = p +1
        r = len(arr)-1
        while(q<r):
            val = arr[p]+ arr[q] + arr[r]
            #print("val: ",val)
            #print("p: ",p)
            #print("q: ",q)
            #print("r:",r)
            if val == 0:
                output.append(p)
                output.append(q)
                output.append(r)
                return output
            elif val > 0:
                r-=1 
            else:
                q+=1
    output.append(-1)
    return output

def makelist(arr,start,end):
    z = []
    for i in range(start,end):
        z.append(arr[i])
    return z 

a = [] 
#file = open("rosalind_3sum.txt","r")
file = open("3sumTest.txt","r")
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
#f = open("3SumOut.txt","w")
for i in range(0,len(a)):
    z = Threesum(a[i])
    for j in range(0,len(z)):
        print(z[j]," ")
    
