max = 0
index = -1
for i in range(9):
    a=int(input())
    if(max < a):
        max = a
        index = i
print(max)
print(index+1)
