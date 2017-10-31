import csv
from tqdm import tqdm
from time import sleep
import json
url_id=[]
with open('ava_train_v1.0.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    column = [row[0] for row in reader]
f=open('id_list.txt', 'a')
j=0
for i in tqdm(column):
    sleep(0.01)
    if i not in url_id:
        url_id.append(i)
        f.write(i+'\n')
        j += 1

f.close()