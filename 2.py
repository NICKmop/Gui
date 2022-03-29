from datetime import datetime, timedelta
import os , openpyxl, logging,logging.handlers
from tkinter import *
from tkinter import messagebox

log_today = datetime.now();
log_today = str(log_today).split(" ")[0];

log = logging.getLogger("C:/Users/user/OneDrive - 대한광통신/바탕 화면/예약/folderList_"+str(log_today)+".log");
log.setLevel(logging.DEBUG);
fileHandler = logging.FileHandler("C:/Users/user/OneDrive - 대한광통신/바탕 화면/예약/folderList_"+str(log_today)+".log");
streamHadler = logging.StreamHandler();

log.addHandler(fileHandler);
log.addHandler(streamHadler);


# gui 해당 루트 선택 input값으로.
directory = r'\\10.12.11.20\TFO.FAIT.Share';

dest_filename = 'folderList.xlsx';
load_monitoring = openpyxl.load_workbook(dest_filename);

root = Tk();
root.title("folder Scan");
root.geometry("640x480")


def run_fast_scandir(dir):   
    subfolders = [];
    try:
        for f in os.scandir(dir):
            if f.is_dir():
                subfolders.append(f.path)
    except PermissionError as ps:
        print(ps);
        pass


    for dir in list(subfolders):
        sf = run_fast_scandir(dir)
        subfolders.extend(sf)
    return subfolders;

def excelWrite(folderPath, Path):
    load_ws = load_monitoring['Sheet1'];
    for i in range(1, len(folderPath)):
        load_ws['A'+str(i)].value = '=HYPERLINK("{}")'.format(folderPath[i]);

    load_monitoring.save(Path);




root.mainloop()  # 창이 닫히지 않게 해주는 것

# subfolders = run_fast_scandir(directory);

# excelWrite(subfolders, dest_filename);






