m1=int(input("Enter mark for 1st subject:"))
m2=int(input("Enter mark for 2nd subject:"))
m3=int(input("Enter mark for 3rd subject:"))
avg=((m1+m2+m3)/3)
print(avg)
if (avg>80):
	print("O grade")
elif (avg>70):
	print("A+ grade")
elif (avg>60):
	print("A grade")
elif (avg>50):
	print("B grade")
else:
	print("fail")
