def part(arr):
    a = []
    b = []
    c = []
    a.append(arr[0])
    for i in range(1,len(arr)):
        if(arr[i]>a[0]):
            b.append(arr[i])
        elif(arr[i]==a[0]):
            a.append(arr[i])
        else:
            c.append(arr[i])
    out = []
    for i in range(0,len(c)):
        out.append(c[i])
    for i in range(0,len(a)):
        out.append(a[i])
    for i in range(0,len(b)):
        out.append(b[i])
    f = open("3way.txt","w")
    for i in range(0,len(out)):
        f.write(str(out[i]) + " ")

file = open("rosalind_par3.txt","r")
#file = open("3wayTest.txt","r")
list = []
input = []
for line in file:
    list += line.split()
for i in range(0,len(list)):
    input.append(int(list[i]))
sizeA = input[0]
A = []
for i in range(1,sizeA+1):
    A.append(input[i])
part(A)