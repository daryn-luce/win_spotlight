import os
import filecmp
import pygame
from shutil import copyfile

pic_dir = "C:\\Users\\" + os.getlogin() + "\\Pictures\\wpp\\"
spotlight_dir = "C:\\Users\\" + os.getlogin() + "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\"

def getFiles(spot_dir, save_dir):
	for files in os.listdir(spot_dir):
		if (os.path.getsize(spot_dir + files) > 100000):
			copyfile(spot_dir + files,save_dir + files + ".png")
			tempimg = pygame.image.load(save_dir + files + ".png")
			if(tempimg.get_width() != 1920):
				os.remove(save_dir + files + ".png")

def removeDuplicates(dir):
	del_files = []
	for files in os.listdir(dir):
		for comp_files in os.listdir(dir):
			if(files != comp_files):
				if(filecmp.cmp(dir + files, dir + comp_files)):
					#print("Removing file" + files + " becuase it's a duplicate")
					del_files.append(files)
	for file in del_files:
		if(file[:9] != "Spotlight"):
			os.remove(dir + file)
			
		
def renameWallPaper(dir):
	i = 0
	for files in os.listdir(dir):
		i += 1
		os.rename(dir + files, dir + "Spotlight_wp" + str(i))
	for files in os.listdir(dir):
		os.rename(dir + files, dir + files + ".png")

#print(filecmp.cmp(pic_dir + "\\a.jpg", pic_dir + "\\c.jpg"))
#print(pygame.image.load(pic_dir + "\\a.jpg").get_width())
# copyfile(pic_dir + "\\a", pic_dir + "\\new\\a.jpg")
	
if(os.path.isdir(pic_dir)):
	#curLen = (len(os.listdir(pic_dir)) + 1)
	getFiles(spotlight_dir, pic_dir)
	removeDuplicates(pic_dir)
	renameWallPaper(pic_dir)
	
else:
	os.mkdir(pic_dir)
	getFiles(spotlight_dir, pic_dir)
	