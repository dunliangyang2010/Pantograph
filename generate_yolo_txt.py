import os
import numpy as np

imgfolder = "labelIMG224"    # 圖片路徑
yolofolder = "labelyolo224"    # yolo資料夾的路徑
train_txt_path = "labelcfg224/train.txt"    # 儲存train.txt的路徑
valid_txt_path = "labelcfg224/valid.txt"    # 儲存valid.txt的路徑

allimg = os.listdir(imgfolder)
data_num = len(allimg)
indexes = np.random.permutation(data_num)

train_indexes = indexes[:int(data_num * 0.8)]
valid_indexes = indexes[int(data_num * 0.8):]

f_train = open(train_txt_path, 'w')
for index in train_indexes:
    filename = os.path.join(yolofolder, allimg[index])
    f_train.write(filename+'\n')
    print(filename)
f_train.close()

f_valid = open(valid_txt_path, 'w')
for index in valid_indexes:
    filename = os.path.join(yolofolder, allimg[index])
    f_valid.write(filename+'\n')
    print(filename)
f_valid.close()