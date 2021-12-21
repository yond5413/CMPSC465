def fibonacci(x):
    if x == 0:
        return 0
    elif x ==1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
'''file = open("rosalind_fibo.txt","r")
lines = []
for line in file.readline():
    lines.append(line)
input = []
for i in range(1,len(lines)):
    input[i] = int(lines[i])

for i in range(1,len(input)):
    print(input[i])'''
print(fibonacci(24))