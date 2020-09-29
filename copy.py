copy = input("Please enter the full name and path of the document you would like to copy ex.test/file.txt: ")
paste = input("Please enter where you would like to copy this file to: ")

file = open(copy, 'r+')
paster = open(paste, 'w')
f = file.readlines()

for line in f:
	paster.write(line)
	print(line)
file.close()
paster.close()
input("\nCopying successful press ENTER to continue")