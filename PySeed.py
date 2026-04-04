import secrets
import os

seeds = []
for thing in range(64):

 done = secrets.token_hex(16)
 print('result', done)
 seed = int(done, 16)
 n = seed % (2 ** 64)

 # translate to Minecraft Java
 if n >= 2 ** 63:
     n -= 2 ** 64
 print('Minecraft seed', n)
 seeds.append(n)

home = os.path.expanduser('~')
downloads_folder = os.path.join(home, 'Downloads')
if not os.path.exists(downloads_folder):
    os.mkdir(downloads_folder)
file_name = "seeds.txt"
file_path = os.path.join(downloads_folder, file_name)
with open(file_path, 'a') as new_file: # change (file_path, 'a') to (file_path, 'w') if you want it to overwrite
    for seed in seeds:
        new_file.write(f"{seed}\n")
