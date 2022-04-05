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
fileTimeBox = [];
fileExe = [];
cnt = 0;
for (path, dir, file) in os.walk(path_dir):
    
    fileTimeBox = [];
    fileExe = [];

    folderScan = {
        "path":path,
        "dir" : dir,
        "file": file
    }

    for i in folderScan['file']:
        try:
            fileMtime = datetime.fromtimestamp(os.path.getmtime(path+'\\'+i));
            print(fileMtime);
            fileTimeBox.append(str(fileMtime).split('.')[0])
            folderScan["fileCreateTime"] = fileTimeBox;
        except OSError as os:
            print(os);
            pass;
        except NameError as name:
            print(name)
            pass;
    for j in folderScan["file"]:
        name, ext = os.path.splitext(j);
        if not ext:
            ext = "확장자가 없습니다."
        fileExe.append(ext);
        folderScan["fileExe"] = fileExe;

    folderInfo.append(folderScan);

jsonFileInput(folderInfo);  
    # cnt += 1;
    # if cnt == 100:
    #     jsonFileInput(folderInfo);
    #     break
   

