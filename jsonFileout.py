#-*- coding:utf-8 -*-
from datetime import datetime
import os, json

path_dir = r'\\10.12.11.20\TFO.FAIT.Share'

def jsonFileInput(value):
    with open("folderScanfile.json", "w", encoding='utf-8') as json_file:
    # with open("folderScan.json", "w", encoding='utf-8') as json_file:
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
        "dir" :dir,
        "file":file
    }

    # 파일 들의 확장자 및 파일명 체크
    if not folderScan['file']:
        folderScan["fileCreateTime"] = fileTimeBox;
        folderScan["fileExe"] = fileExe;
    else:
        for i in folderScan['file']:
            
            try:
                # fileMtime = datetime.fromtimestamp(os.path.getctime(path+'\\'+i.split(":")[1]));
                fileMtime = datetime.fromtimestamp(os.path.getctime(path+'\\'+i));
                name, ext = os.path.splitext(i);

                if not ext:
                    ext = "확장자가 없습니다."
                elif not name:
                    name = "파일명이 없습니다."
                
            except OSError as os:
                pass;
            except NameError as name:
                pass;
            fileTimeBox.append(str(fileMtime).split('.')[0])
            folderScan["fileCreateTime"] = fileTimeBox;
            fileExe.append(ext);
            folderScan["fileExe"] = fileExe;

    folderInfo.append(folderScan);

jsonFileInput(folderInfo);  
    # cnt += 1;
    # if cnt == 100:
    #     jsonFileInput(folderInfo);
    #     break
   

