#-*- coding:utf-8 -*-
from dataclasses import replace
import os, json
from posixpath import split

path_dir = r'\\10.12.11.20\TFO.FAIT.Share'


def jsonFileInput(value):
    with open("folderScan.json", "w", encoding='utf-8') as json_file:
        json.dump(value, json_file, ensure_ascii=False);

folderInfo = [];
cnt = 0;
for (path, dir, file) in os.walk(path_dir):
    # path = path.replace("\\","\'");
    # path = path.replace("\\\\",r"\\");
    folderScan = {
        "path":path,
        "dir" : dir,
        "file": file
    }
    cnt += 1;
    folderInfo.append(folderScan);
    if cnt == 10:
        jsonFileInput(folderInfo);
        break
   

