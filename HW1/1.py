##my_list = ["item1", "item2", "item3", "item4"]
##FOLDER_PATH = r'C:\\Users\\Jinzhi Shen\\Desktop\\602\\HW1'
import os

file_path = r'C:\\Users\\Jinzhi Shen\\Desktop\\602\\HW1'

if os.path.exists(file_path):
    st = os.stat(file_path)
    mode = st.st_mode
    owner_permissions = (mode & 0o700) >> 6  # 获取文件所有者权限
    print(f"Owner permissions: {oct(owner_permissions)}")
else:
    print("File not found.")

##　rwx    7
##  rw-    6
##  r-x    5
##  -wx    3
##  r--     4
##  -w-    2
##  --x    1