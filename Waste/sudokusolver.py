#List of list of elements in each column
sudoku = [['9', '8', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '3', '6', '_', '7', '_', '5', '_'], ['_', '_', '_', '_', '_', '_', '3', '_', '_'], ['_', '1', '_', '_', '3', '_', '_', '7', '_', '8'], ['_', '_', '_', '_', '9', '5', '_', '4', '_', '', '', '', '', '', '', '', ''], ['2', '_', '_', '_', '_', '_', '_', '_', '5'], ['_', '_', '7', '_', '_', '9', '_', '6', '_'], ['_', '_', '_', '_', '5', '_', '_', '_', '_'], ['_', '_', '6', '_', '3', '_', '8', '7', '_']]
"""for i in range(9):
	print("Enter elements in column{}".format(i+1))
	elements = input()
	sudoku.append(elements.split(" "))
#print(sudoku)"""


#Function to check element in column
def check_in_column(arg,column):
	if str(arg) not in sudoku[column-1]:
		return arg
#Function to check element in row
def check_in_row(arg,row):
	for i in range(9):
		if str(arg) in sudoku[i][row-1]:
			return
	return arg
#Function to createblock from th input
def create_block(sudoku):
	Block_set = []
	for i in range(0,9,3):
		block = sudoku[i][0:3]+sudoku[i+1][0:3]+sudoku[i+2][0:3]
		Block_set.append(block)
	for i in range(0,9,3):
		block = sudoku[i][3:6]+sudoku[i+1][3:6]+sudoku[i+2][3:6]
		Block_set.append(block)
	for i in range(0,9,3):
		block = sudoku[i][6:9]+sudoku[i+1][6:9]+sudoku[i+2][6:9]
		Block_set.append(block)
	return Block_set

Block = create_block(sudoku)
#print(create_block(sudoku))

#function to check element in a block
def check_in_block(arg,block):
	if str(arg) in Block[block-1]:
		return 
	return arg
#print(check_in_block(9,1))
Set = {}
for i in range(9):
	for j in range(9):
		if sudoku[i][j] == "_":
			element_address = str(i+1)+str(j+1)
			Set[element_address] = []

#Everythng is fine till here Now gonnna change something but remember everythng is safe till here 

	

































