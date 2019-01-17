import os
import filecmp
import pygame
from shutil import copyfile

# The two directories we're working with (pictures\wp and spotlight), file type and naming scheme
pic_dir = "C:\\Users\\" + os.getlogin() + "\\Pictures\\wp\\"
spotlight_dir = "C:\\Users\\" + os.getlogin() + "\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\"
file_type = ".jpg"
name_scheme = "Spotlight_wp"



# gets copies the files from the spotlight dir to the picture dir
# as long as it's greater than 100kb and has a width of 1920px
def getFiles(spot_dir, save_dir):
	for files in os.listdir(spot_dir):
		if (os.path.getsize(spot_dir + files) > 100000):
			copyfile(spot_dir + files,save_dir + files + file_type)
			tempimg = pygame.image.load(save_dir + files + file_type)
			if(tempimg.get_width() != 1920):
				os.remove(save_dir + files + file_type)



# Removes duplicates by looping through the directory twice and
# ignoreing files with the same name then collects duplicates
# Then goes through the duplicate list and removes any wallpapers
# we don't already have.
def removeDuplicates(dir):
	del_files = []
	for files in os.listdir(dir):
		for comp_files in os.listdir(dir):
			if(files != comp_files):
				if(filecmp.cmp(dir + files, dir + comp_files)):
					if(files not in del_files):
						del_files.append(files)
	for file in del_files:
		if(file[:12] != name_scheme):
			os.remove(dir + file)
	

	
# renames the contents of the directoy for readability and so 
# we can check new files with ones we already have. through our 
# naming scheme		
def renameWallPaper(dir):
	i = 0
	for files in os.listdir(dir):
		i += 1
		os.rename(dir + files, dir + name_scheme + str(i))
	for files in os.listdir(dir):
		os.rename(dir + files, dir + files + file_type)



# checks if directory exsist(creates it otherwise), then runs our functions
# first getting the images, then removing duplicates, finally renaming.	
if(os.path.isdir(pic_dir)):
	getFiles(spotlight_dir, pic_dir)
	removeDuplicates(pic_dir)
	renameWallPaper(pic_dir)
else:
	os.mkdir(pic_dir)
	getFiles(spotlight_dir, pic_dir)
	removeDuplicates(pic_dir)
	renameWallPaper(pic_dir)
