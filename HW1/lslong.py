#!/usr/bin/env python3
import os
import datetime
import grp
import stat
import pwd

script_path = os.path.abspath(__file__)
script_folder = os.path.dirname(script_path)
##print(script_folder)
##FOLDER_PATH = r'C:\\Users\\Jinzhi Shen\\Desktop\\602\\HW1'
def lslong(dir="."):
    fileNames = os.listdir(dir)
    fileNames.sort(key = custom_key)
##    for fileName in fileNames:
##        print('File Name:' + fileName)
    file_details = []
    max_size_length = 0
    max_link_length = 0
    blue_text = "\033[34m"
    reset_color = "\033[0m"
    for fileName in fileNames:
        entry_path = os.path.join(dir, fileName)
        file_stat = os.stat(entry_path)

        details = {}

        details['file'] = fileName
        if os.path.isdir(entry_path):
            # Add a trailing '/' for directories
            details['file'] = blue_text + fileName+ reset_color

        else:
            fileName =fileName
    # add the time of the file___________________________
        time = os.path.getmtime(entry_path)
  
    # Convert the modification time to a human-readable date and time
        modification_time_datetime = datetime.datetime.fromtimestamp(time)

    # Format the datetime as a string in a desired format
        
        formatted_time = modification_time_datetime.strftime('%b %d %H:%M')
        details['time'] = formatted_time

    # add the size of the file __________________________________
        file_size = os.path.getsize(entry_path)
        details['file_size'] = file_size 

    # add the group of the file __________________________________
        file_info = os.stat(entry_path)
        gid = file_info.st_gid
        group_info = grp.getgrgid(gid)
        group_name = group_info.gr_name
        details['group'] = group_name
        
    # add the owner of the file
        file_info_2 = os.stat(entry_path)
        gid_2 = file_info_2.st_gid
        owner_info = pwd.getpwuid(gid_2)
        owner_name = owner_info.pw_name
        details['owner'] = owner_name

    # grab the permission of the current file
        details['permissions'] = stat.filemode(file_stat.st_mode)
  
    # grab the number of links        
        details['num_links'] = file_stat.st_nlink

    # find the max of size and # of links so that they could be aligned when printed   
        max_size_length = max(max_size_length, len(str(details['file_size'])))
        max_link_length = max(max_link_length, len(str(details['num_links'])))
        
        file_details.append(details)

    for details in file_details:
        print(f"{details['permissions']} {str(details['num_links']).rjust(max_link_length)} {details['owner']} {details['group']} {str(details['file_size']).rjust(max_size_length)} {details['time']} {details['file']}")
        
def custom_key(item):
    if isinstance(item, str):
       return item 
    else:
        return sdtr(item)    
 


if __name__ == "__main__":
##    listDir(FOLDER_PATH) 
      lslong()    
