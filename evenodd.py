l2=[]
even=[]
odd=[]
l1=int(input("Enter the number of elements:"))

for i in range(l1):
	a=int(input("enter the no:"))
	l2.append(a)
print(l2)
for j in l2:
	if (j%2==0):
		even.append(j)
	
	else:
		odd.append(j)
print("even no:",even)
print("odd no:",odd)
	
