
import os
import time

downloadpath = r"/downloads"
destinationpath = r"/destination"

#move files function
def move_files(dowloadpath, destinationpath):
        #move files
        for file in os.listdir(dowloadpath):
            os.replace(os.path.join(dowloadpath, file), os.path.join(destinationpath, file))
        print("Files moved successfully.")

#delete files function
def delete_files_is_same(downloadpath, destinationpath):
        if(len(os.listdir(downloadpath)) > 0):
            #delete file from dowload if same file exists in destination
            for file in os.listdir(destinationpath):
                for file2 in os.listdir(downloadpath):
                    if(file == file2):
                        os.remove(os.path.join(downloadpath, file2))
                        print ("File " + file2 + " deleted successfully.")
while True:
    #check if path exists
    if(os.path.exists(downloadpath) and os.path.exists(destinationpath)):
        print("Path exists.")
        #check for duplicate files in download and destination
        delete_files_is_same(downloadpath, destinationpath)
        
    else:
        print("Path does not exist.")
    
    time.sleep(60)