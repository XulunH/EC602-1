#!/usr/bin/env python3
import os

##from colorama import Fore
script_path = os.path.abspath(__file__)
script_folder = os.path.dirname(script_path)
##print(script_folder)
##FOLDER_PATH = r'C:\\Users\\Jinzhi Shen\\Desktop\\602\\HW1'
def lscol(dir="."):
    fileNames = os.listdir(dir)
    fileNames.sort(key = custom_key)
##    for fileName in fileNames:
##        print('File Name:' + fileName)
    terminal_size = os.get_terminal_size()
    terminal_width = terminal_size.columns
    n = find_the_n(terminal_width, fileNames)
    #print(n)
    blue_text = "\033[34m"
    reset_color = "\033[0m"
    for fileName in fileNames:
        entry_path = os.path.join(dir, fileName)
        ##if os.path.isdir(entry_path):
            # Add a trailing '/' for directories
 ##           fileName = blue_text + fileName+ reset_color
## remember we need a edge case where there is nothing in the folder. which I don't know is necessary or not


    # now let's print according to n
    sublists = [fileNames[i::n] for i in range(n)]
    #print(sublists)
    column_widths = [len(item) for item in sublists[0]]
    for row in sublists:
        for i, item in enumerate(row):
            column_widths[i] = max(column_widths[i], len(item)) 
    new_column_widths = [elements + 2 for elements in column_widths]       
    #print(new_column_widths)
    
    for row in sublists:
        for item, width in zip(row, new_column_widths):
            entry_path = os.path.join(dir, item)
            if os.path.isdir(entry_path):
            
               print(f"{blue_text + fileName+ reset_color:<{width}}", end = "")
            ##print (width)
            else:
               print(f"{item:<{width}}", end = "")
        print()
    

def find_the_n(screen_size, list):
    length = 0
    ##print(screen_size)
    ##print(list)
    for i in range(len(list)):
        n = i + 1
        length = find_the_width(list, n)
        #print(length)
        if length <=  screen_size:
            return n
         
        

### this will be a function that find the width that will be taken with n rows:
def find_the_width(list, n):
    #print("I hit this func")
    #print(n)
     # Split the list into n parts along the first dimension
    split_lists = [list[i::n] for i in range(n)]
    ### e.x. [[1, 3, 5], [2, 4, 6]]
    #print(split_lists)
    total_max_length = 0

## find how many 2s we need to add to the width 
    max_content_count = 1 
    for sublist in split_lists:

        content_count = len(sublist)
        if content_count > max_content_count:
            max_content_count = content_count



## now let's find the width caused only by the contens
    longest_strings = []
    max_length = max(len(seq) for seq in split_lists)
    for i in range(max_length):
        column = [seq[i] if i<len(seq) else "" for seq in split_lists]
        longest_in_column = max(column,key=len)
        longest_strings.append(longest_in_column)
    total_length = sum (len(longest) for longest in longest_strings)
    #print(total_length)
    
    return total_length + 2*(max_content_count - 1)

# Calculate the sum of maximum values for each column
    ##column_sums = sum(max(sublist[col] for sublist in split_lists) for col in range(len(list[0])))
def custom_key(item):
    if isinstance(item, str):
       return item 
    else:
        return sdtr(item)    

if __name__ == "__main__":
##    listDir(FOLDER_PATH) 
      lscol() 
