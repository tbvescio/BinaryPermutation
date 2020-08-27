entrada = int(input("Enter the number of variables: "))

for i in range(2**entrada): 
	row = list(bin(i)[2:]) #removes the '0b' from the result of bin()
	for x in range(entrada-len(row)): 
		row.insert(0, '0')
	print(row)





