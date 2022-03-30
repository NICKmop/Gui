import os

path_dir = ''

for (path, dir, file) in os.walk(path_dir):

    print("path : ",path)

    print("dir : ",dir)

    print("file : ",file)

    print("===============")