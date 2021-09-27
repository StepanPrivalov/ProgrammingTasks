
#1
name = "Steve"
secondName = "Privalov"
yearOfBirth = "2004"

print(name,secondName,yearOfBirth, sep = "_")

#2
print("Enter catets: ")
a = int(input())
b = int(input())
c = (a**2 + b**2)**0.5
print("Ploshad =", a*b/2)
print("Perimetr =", a+b+c)

#3
print("Enter radius: ")
radius = int(input())
print("Ploshad kruga =", radius**2 * 3.14)

#4

print("How much years do we have - ", end = "")
years = int(input())

time = years * 365 * 24 * 60
print("Time in minutes -", time)
print("With so much time u'll see", time//5, "exponauts")

print("How much exponats do we have - ", end = '')
exponauts = int(input())

print(exponauts * 5, "minutes u need to see all of these")
print(exponauts * 5 // 60, " hours u need")
print(exponauts * 5 // 60// 24, "days u need")
print(exponauts * 5 // 60// 24 // 365, "years u need")













