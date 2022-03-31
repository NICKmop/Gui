import json

with open('folderScan.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f);


fileBox = [];

for i in range(0,len(json_data)):
    path = json_data[i]['path'];
    dir = json_data[i]['dir'];
    file = json_data[i]['file'];

    for i in file:
        print(i);
        # fileBox.append(file)
    
