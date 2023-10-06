import os
import datetime

script_path = os.path.abspath(__file__)
script_folder = os.path.dirname(script_path)
##print(script_folder)
##FOLDER_PATH = r'C:\\Users\\Jinzhi Shen\\Desktop\\602\\HW1'
def listDir(dir):
    fileNames = os.listdir(dir)
##    for fileName in fileNames:
##        print('File Name:' + fileName)
    for fileName in fileNames:
        entry_path = os.path.join(dir, fileName)
    # add the time of the file___________________________
        time = os.path.getmtime(entry_path)

    # Convert the modification time to a human-readable date and time
        modification_time_datetime = datetime.datetime.fromtimestamp(time)
        print(modification_time_datetime)
    
        formatted_time = modification_time_datetime.strftime('%b %d %H:%M:%S')
        print(formatted_time)

month_dict = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}

if __name__ == "__main__":
##    listDir(FOLDER_PATH) 
      listDir(script_folder)    
