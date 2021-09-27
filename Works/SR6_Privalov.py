a = []
print("Enter the number of elements: ", end = "")
n = int(input())

for i in range(n):
    elem = int(input())
    a.append(elem)

for i in range(n - 1):
    for j in range(i, n):
        if a[i] > a[j]:
            a[j], a[i] = a[i], a[j]

print("Enter delta: ", end = "")
delta = int(input())
kolvo = 0

for num in a:
    if num == a[0] + delta:
        kolvo += 1

print(kolvo)
     
