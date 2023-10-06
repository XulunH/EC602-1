#!/usr/bin/env python3
import os

script_path = os.path.abspath(__file__)
script_folder = os.path.dirname(script_path)
##print(script_folder)
##FOLDER_PATH = r'C:\\Users\\Jinzhi Shen\\Desktop\\602\\HW1'
def lsfiles(dir="."):
    fileNames = os.listdir(dir)
##    for fileName in fileNames:
##        print('File Name:' + fileName)

    fileNames.sort(key = custom_key)
    for fileName in fileNames:
        entry_path = os.path.join(dir, fileName)
        if os.path.isdir(entry_path):
            # Add a trailing '/' for directories
           # print(blue_text + fileName+ reset_color)
           pass
        else:
            print(fileName, end = " ")
    print('\n')
    for fileName in fileNames:
        entry_path = os.path.join(dir, fileName)
        if os.path.isdir(entry_path):
            # Add a trailing '/' for directories
           # print(blue_text + fileName+ reset_color)
           print(fileName + ":")
           listDir_help(entry_path)
           print('\n')
  
def custom_key(item):
    if isinstance(item, str):
       return item 
    else:
        return sdtr(item) 

def listDir_help(dir):
    fileNames = os.listdir(dir)
##    for fileName in fileNames:
##        print('File Name:' + fileName)
    blue_text = "\033[34m"
    reset_color = "\033[0m"
    fileNames.sort(key = custom_key)
    for fileName in fileNames:
        entry_path = os.path.join(dir, fileName)
        if os.path.isdir(entry_path):
            # Add a trailing '/' for directories
            print(blue_text + fileName+ reset_color,end = ' ')
        else:
            print(fileName, end = ' ')   

if __name__ == "__main__":
##    listDir(FOLDER_PATH) 
      lsfiles(script_folder)  
        
        
            
         
   
