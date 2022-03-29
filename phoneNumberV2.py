import re ,logging, logging.handlers, xlrd
from bs4 import BeautifulSoup;
import openpyxl
from sre_constants import SUCCESS
from datetime import datetime, timedelta
from openpyxl import load_workbook

log_today = datetime.now();
log_today = str(log_today).split(" ")[0];

log = logging.getLogger("C:/Users/user/OneDrive - 대한광통신/바탕 화면/예약/phoneNumberV2"+str(log_today)+".log");
log.setLevel(logging.DEBUG);

fileHandler = logging.FileHandler("C:/Users/user/OneDrive - 대한광통신/바탕 화면/예약/phoneNumberV2"+str(log_today)+".log");
streamHadler = logging.StreamHandler();

old_xlsx = 'C:/Users/user/OneDrive - 대한광통신/바탕 화면/예약/대한광통신 사내전화번호부_20220110.xls'
new_xlsx = 'C:/Users/user/OneDrive - 대한광통신/바탕 화면/예약/대한광통신 사내전화번호부_20220211.xls'

wb1 = xlrd.open_workbook('대한광통신 사내전화번호부_20220110.xls');
wb2 = xlrd.open_workbook('대한광통신 사내전화번호부_20220211.xls');

def wbCount(wb1, wb2):
    wb1Rows = 0;
    wb2Rows = 0;

    wb1Array = [];
    wb2Array = [];

    sheet1Wb = [];
    # dt.append(wb1Sheet.row_values(i));

    for i in range(0,9):
        wb1Sheet = wb1.sheet_by_index(i);
        wb1Rows = wb1Sheet.nrows;

        wb2Sheet = wb2.sheet_by_index(i);
        wb2Rows = wb2Sheet.nrows;

        if i == 0:
            for i in range(wb1Rows):
                wb1Array.append(wb1Sheet.row_values(i));
            for i in range(wb2Rows):
                wb2Array.append(wb2Sheet.row_values(i));
        if i == 1:
            for i in range(wb1Rows):
                wb1Array.append(wb1Sheet.row_values(i));
            for i in range(wb2Rows):
                wb2Array.append(wb2Sheet.row_values(i));
        if i == 2:
            for i in range(wb1Rows):
                wb1Array.append(wb1Sheet.row_values(i));
            for i in range(wb2Rows):
                wb2Array.append(wb2Sheet.row_values(i));
        if i == 3:
            for i in range(wb1Rows):
                wb1Array.append(wb1Sheet.row_values(i));
            for i in range(wb2Rows):
                wb2Array.append(wb2Sheet.row_values(i));
        if i == 4:
            for i in range(wb1Rows):
                wb1Array.append(wb1Sheet.row_values(i));
            for i in range(wb2Rows):
                wb2Array.append(wb2Sheet.row_values(i));
        if i == 5:
            for i in range(wb1Rows):
                wb1Array.append(wb1Sheet.row_values(i));
            for i in range(wb2Rows):
                wb2Array.append(wb2Sheet.row_values(i));
        if i == 6:
            for i in range(wb1Rows):
                wb1Array.append(wb1Sheet.row_values(i));
            for i in range(wb2Rows):
                wb2Array.append(wb2Sheet.row_values(i));
        if i == 7:
            for i in range(wb1Rows):
                wb1Array.append(wb1Sheet.row_values(i));
            for i in range(wb2Rows):
                wb2Array.append(wb2Sheet.row_values(i));
        if i == 8:
            for i in range(wb1Rows):
                wb1Array.append(wb1Sheet.row_values(i));
            for i in range(wb2Rows):
                wb2Array.append(wb2Sheet.row_values(i));
        if i == 9:
            for i in range(wb1Rows):
                wb1Array.append(wb1Sheet.row_values(i));
            for i in range(wb2Rows):
                wb2Array.append(wb2Sheet.row_values(i));
        

    return wb1Rows, wb2Rows, wb1Array, wb2Array;

print(wbCount(wb1, wb2));
# 0 ~ 8
# wb1Count = wbCount(wb1, wb2)[0];
# wb1SheetData = wbCount(wb1, wb2)[2];

# wb2Count = wbCount(wb1, wb2)[1];
# wb2SheetData = wbCount(wb1, wb2)[3];

# print(wb1SheetData);

# arrayDt = [];
# if wb1Count > wb2Count:
    # for i in range(wb1Count):
    #     arrayDt.append(wb1SheetData.row_values(i))
    #     print(arrayDt);
# else:
#     print('1일 더 큼')



