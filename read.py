import ctypes
txt = input("Please enter the full name and path of the file you would like to read: ")
file = open(txt, 'r')
f = file.readlines()

textList = []
for line in f:
	print(line, "\n")
	textList.append(line.strip())

print(textList)
input("\nRead successful press ENTER to continue\n")