#-*- coding:utf-8 -*-
from dataclasses import replace
from posixpath import split
from datetime import datetime
import os, json

path_dir = r'\\10.12.11.20\TFO.FAIT.Share'


def jsonFileInput(value):
    with open("folderScan.json", "w", encoding='utf-8') as json_file:
        json.dump(value, json_file, ensure_ascii=False);

folderInfo = [];
cnt = 0;
for (path, dir, file) in os.walk(path_dir):
    # path = path.replace("\\","\'");
    # path = path.replace("\\\\",r"\\");
    for fileTime in file:
        fileMTime = datetime.fromtimestamp(os.path.getmtime(fileTime));
    folderScan = {
        "path":path,
        "dir" : dir,
        "file": file,
        "fileTime": fileMTime 
    }
    
    folderInfo.append(folderScan);

# jsonFileInput(folderInfo);  
    cnt += 1;
    if cnt == 10:
        jsonFileInput(folderInfo);
        break
   

