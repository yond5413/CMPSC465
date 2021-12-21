# importing the sys module
import random 
def median(Arr,k):
    sL = []
    sV = []
    sR = []
    v = Arr[random.randint(0,len(Arr)-1)]
    for i in range(0,len(Arr)):
        if Arr[i] < v:
            sL.append(Arr[i])
        elif Arr[i] == v:
            sV.append(Arr[i])
        else:
            sR.append(Arr[i])
    if k <= len(sL):
        return median(sL,k)
    elif len(sL) < k and k<= (len(sL) +len(sV)):
        return sV[0] # all entries are the same
    elif k > (len(sL)+len(sV)):
        return median(sR,k -(len(sL)+len(sV)))
   
   # return None
a = []
#median(a,8)
#print(median(a,8))
file = open("rosalind_med.txt","r")
#file = open("Median.txt","r") # same as sample datasheet
list = []
input = []
for line in file:
    list += line.split()
for i in range(0,len(list)):
    input.append(int(list[i]))
sizeA = input[0]
for i in range(1,sizeA+1):
    a.append(input[i])
print(median(a,input[len(input)-1]))
