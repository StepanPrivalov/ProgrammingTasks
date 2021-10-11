print("Enter the array in one string: ", end="")
s = input()
ar = s.split()
a = []
for i in range(len(ar)):
    if ar[i].isdigit() == True:
        a.append(int(ar[i]))
    else:
        print("No letters or words allowed!!")
        
print(*a)

for i in range(len(a) - 1):
    for j in range(i, len(a)):
        if a[i] > a[j]:
            a[j], a[i] = a[i], a[j]

print("Enter delta: ", end = "")
delta = int(input())
kolvo = 0

for num in a:
    if num == a[0] + delta:
        kolvo += 1

print(kolvo)
     
