import os
file = input("Enter the full name and path of file would you like to rename ex. test/file.txt: ")
rename = input("Enter what you would like to rename the file to: ")

os.rename(file, rename)

input("\nRenaming successful press ENTER to continue\n")