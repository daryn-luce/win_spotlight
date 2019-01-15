import os
import filecmp
import pygame
from shutil import copyfile

pic_dir = "C:\\Users\\" + os.getlogin() + "\\Pictures\\wp"
spotlight_dir = "C:\\Users\\" + os.getlogin() + "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"


#print(filecmp.cmp(pic_dir + "\\a.jpg", pic_dir + "\\c.jpg"))
#print(pygame.image.load(pic_dir + "\\a.jpg").get_width())
# copyfile(pic_dir + "\\a", pic_dir + "\\new\\a.jpg")
	
# if(os.path.isdir(pic_dir)):
	# #copyfile("C:\\Users\\" + os.getlogin() + "\\Pictures\\test.txt", pic_dir + "\\test.txt")
# else:
	# os.mkdir(pic_dir)
def removeDup():
	i = 1
	
	for files in os.listdir(pic_dir):
		print(i)
		print(files)
		try:
			if(filecmp.cmp(pic_dir + "\\" + str(i) + ".jpg", pic_dir + "\\" + files)):
				print("")
			else:
				os.remove(pic_dir + "\\" + str(i) + ".jpg")
		except:
			print("no files move on")
		i += 1
def renamePic():
	i = 0
	for files in os.listdir(pic_dir):
		i += 1
		os.rename(pic_dir + "\\" + files, pic_dir + "\\" + str(i))
	i = 0
	for files in os.listdir(pic_dir):
		i += 1
		os.rename(pic_dir + "\\" + files, pic_dir + "\\" + str(i) + ".jpg")
curLen = (len(os.listdir(pic_dir)) + 1)
for files in os.listdir(spotlight_dir):
	if (os.path.getsize(spotlight_dir + "\\" + files) > 150000):
		renamePic()
		copyfile(spotlight_dir + "\\" + files,pic_dir + "\\" + files + ".jpg")
		tempimg = pygame.image.load(pic_dir + "\\" + files + ".jpg")
		if(tempimg.get_width() == 1920):	
			os.rename(pic_dir + "\\" + files + ".jpg",pic_dir + "\\" + str(curLen) + ".jpg")
			# for nxtFile in os.listdir(spotlight_dir):
				# print("_")
			curLen += 1
		else:
			os.remove(pic_dir + "\\" + files + ".jpg")
		#print(files + " [Size:][" + str(os.path.getsize(spotlight_dir + "\\" + files)) + "]")

removeDup()
renamePic()
			