def insertionsort(Arr):
    count = 0
    for i in range(1,len(Arr)):
        k = i
        while k>0 and Arr[k] < Arr[k-1]:
            Arr[k], Arr[k-1] = Arr[k-1],Arr[k]#swap
            k = k-1
            count +=1
    print(count)
    return None

file = open("rosalind_ins.txt","r")
list = []
input = []
for line in file:
    list += line.split()
for i in range(0,len(list)):
    input.append(int(list[i]))
sizeA = input[0]
A = []
for i in range(1,len(input)):
    A.append(input[i])
insertionsort(A)