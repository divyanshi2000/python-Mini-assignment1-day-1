

list = []
n = int(input("enter length"))
i = 1
while i < n + 1:
    e = int(input("enter element"))
    list.append(e)
    i = i + 1
print(list)
even = []
for j in list:
    if (j % 2 == 0):
        even.append(j)
even.sort()
print(even[0])