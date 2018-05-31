dict={'c':3,'a':1,'b':2,'d':4}
print("Initial dictionary\n",dict)
d3=input("enter the key to delete(a-d):")
if d3 in dict:
	del dict[d3]
	print("Update dictionary\n",dict)
