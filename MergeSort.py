count = 0
def mergesort(a):#array a
    a1 =[]
    a2 = []
    if len(a) -1 > 0:
        for i in range(0,int(len(a)/2)):
           a1.append(a[i])
        for i in range(int((len(a))/2), len(a)):
            a2.append(a[i])
        return merge(mergesort(a1),mergesort(a2))
        
    else:
        return a
   
def merge(x,y):
    z = [] # merged list
    xpos = 0
    ypos = 0
    global count
    while((xpos<len(x)) and (ypos < len(y))):
        if(x[xpos] < y[ypos]):
            z.append(x[xpos])
            xpos+=1
            
        else:
            z.append(y[ypos])
            ypos+=1
            count+=1    
    while (xpos < len(x)): 
        z.append(x[xpos])
        xpos +=1
        
    while (ypos < len(y)):
        z.append(y[ypos])
        ypos += 1 
 
    return z   

a = []

file = open("rosalind_ms.txt","r")
#ile = open("MergeTest.txt","r")
list = []
input = []
for line in file:
    list += line.split()
for i in range(0,len(list)):
    input.append(int(list[i]))
sizeA = input[0]
for i in range(1,sizeA+1):
    a.append(input[i])

z = mergesort(a)
f = open("MergesortOut.txt","w")
for i in range(0,len(z)):
    f.write(str(z[i])+" ")


