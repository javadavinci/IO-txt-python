import ctypes
import os
mode = input("Would you like to read(1), write(2), rename(3), or copy(4): ").lower()
if mode=="read" or mode=="1":
	os.system('python read.py')
elif mode=="write" or mode=="2":
	os.system('python write.py')
elif mode=="rename" or mode=="3":
	os.system('python rename.py')
elif mode=="copy" or mode=="4":
	os.system('python copy.py')
else:
	ctypes.windll.user32.MessageBoxW(0, u"Please choose a valid mode", u"Error", 0)