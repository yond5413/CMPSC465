def MajorityElement(arr):
    arr.sort()
    high = 0 # most frequent
    ans = 0
    i = 0
    while(i < len(arr)):
        current = 1
        while(i <len(arr)-1 and arr[i]==arr[i+1]):
            current +=1 
            i+=1
        if(high < current):
            high = current
            ans = arr[i]
        i+=1
    if(len(arr)%2==0):
        if(high > int(len(arr)/2)):
            return ans
        else:
            return -1 
    else:
         if(float(high) > float(len(arr)/2)):
            return ans
         else:
             return -1


def makelist(arr,start,end):
    z = []
    for i in range(start,end):
        z.append(arr[i])
    return z 

a = [] 
file = open("rosalind_maj.txt","r")
#file = open("MajoirtyElement.txt","r")
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
    a.append(makelist(input,index,(size*i)+2))
    i +=1
    index += size
    check+=1
    listcount+=1
f = open("MajorityOut.txt","w")
for i in range(0,len(a)):
    f.write(str(MajorityElement(a[i]))+" ")
   