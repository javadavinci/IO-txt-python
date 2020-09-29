txt = input("Enter full name and path of document you would like to write to ex.'file.txt': ")
write = input("Enter what you want to put in the document: ")
writeNum = int(input("Enter a number: "))
writeNum = str(writeNum*2)
which = input("To overwrite enter 'o' or enter '1', to append enter 'a', or enter '2': ").upper()

if which=="O" or which=="1":
	file = open(txt, 'w')
	file.writelines(write+"\n")
	file.writelines(writeNum+"\n")
	file.writelines(file.name+"\n\n")
elif which=="A" or which=="2":
	file = open(txt, 'a')
	file.writelines(write+"\n")
	file.writelines(writeNum+"\n")
	file.writelines(file.name+"\n\n")
else:
	print("Please choose overwrite or append")

input("\nWrite successful press ENTER to continue\n")