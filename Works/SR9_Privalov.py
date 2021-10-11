def square(a,b):
    d = a * (2**0.5)
    if b >= d:
        print("Yes, u can")
    else:
        print("NONONO")
                
A, D = -1, -1
while A <= 0 or D <= 0:
	try:
		print("Enter the diameter: ")
		D = int(input())
		print("Enter the side of a square: ")
		A = int(input())
	except ValueError:
		print("No letters allowed!!")

square(A, D)
