with open("result.txt","w") as result:
	with open("list3.txt") as file:
		
		for line in file:
			lin = line.split(",")
			result.write(lin[1])
		