dict={1:'abc',2:'xyz',3:'nmr'}
d4=int(input("Enter the key and value:"))
print(dict)
print(d4)
if d4 in dict:
	print("key is present:")
	del dict[d4]
else:
	print("key isn't present:")
 
