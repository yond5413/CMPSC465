import math
def binarysearch(sorted,k):
    start = 0
    end = len(sorted)-1
    while end >= start:
        middle =math.ceil((start+end)/2) # get new middle index for sectiom
        #print("middle = ",middle )
        #print("start end  ",start,end)
        if(sorted[middle] ==k):
            val = middle +1
            return val  ## found k value we were looking for
            #since indexes start at 0
        elif(sorted[middle]>k):
            end -= 1
        elif(sorted[middle]<k):
           start +=   1
    else:
        return -1

file = open("rosalind_bins.txt","r")
list = []
input = []
size_A = 0
size_B = 0
for line in file:
    list += line.split()
for i in range(0,len(list)):
    input.append(int(list[i]))

size_A = input[0]
size_B = input[1]

'''for i in range(2,len(lines)-1):
    input[i] = int(lines[i])'''

A = []
B = []

for i in range(2,size_A+2):
    A.append(input[i])
for i in range(size_A +2,len(input)):
    B.append(input[i])
output = []

for i in range(0,len(B)):
    output.append(binarysearch(A,B[i]))
for k in range(0,len(output)):
    print(output[k], end = " ")

