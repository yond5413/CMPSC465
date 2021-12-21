
def merge(x,y):
    z = [] # merged list
    xpos = 0
    ypos = 0

    while((xpos<len(x)) and (ypos < len(y))):
        if(x[xpos] < y[ypos]):
            z.append(x[xpos])
            xpos+=1
            
        else:
            z.append(y[ypos])
            ypos+=1
            
    while (xpos < len(x)): 
        z.append(x[xpos])
        xpos +=1
 
    while (ypos < len(y)):
        z.append(y[ypos])
        ypos += 1 
 
    return z   
    '''k = len(x)# causes recursion limit and memory error if I increase the limit
    l = len(y)
       if k == 0:
        return y
    if l ==0:
        return x
    z = []
    hold = []
    other = []
    if x[0] <= y[0]:
        z.append(x[0])
        for i in range(1,k):
            hold.append(x[i])
        other = merge(hold,y).copy()
        for i in range(0,l+k):
            z.append(other[i])
        return z
    else:
        z.append(y[0])
        for i in range(1,l):
            hold.append(y[i])
        other = merge(x,hold).copy()
        for i in range(0,l+k):
            z.append(copy[i])
        return z
'''
a = []
b = []
#file = open("rosalind_mer.txt","r")
file = open("MergeTest.txt","r")
list = []
input = []
for line in file:
    list += line.split()
for i in range(0,len(list)):
    input.append(int(list[i]))
print(list)    
sizeA = input[0]
for i in range(1,sizeA+1):
    a.append(input[i])
sizeB = input[sizeA+1]
for i in range(sizeA+2,len(input)):
    b.append(input[i])
'''print(sizeA)
print(sizeB)
print(len(a))
print(len(b))
print(a[0])
print(b[0])'''
for k in range(0,len(merge(a,b))):
    print(merge(a,b)[k], end=" ")
#print(a)