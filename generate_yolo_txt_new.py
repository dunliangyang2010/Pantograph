import os

train_folder = input('enter train folder: ')  # jpg+txt路徑
val_folder = input('enter val folder: ')  # jpg+txt路徑
des_folder = input('enter des folder: ')    # 輸出資料夾的路徑
train_txt_path = os.path.join(des_folder, 'train.txt') # 儲存train.txt的路徑
val_txt_path = os.path.join(des_folder, 'val.txt') # 儲存val.txt的路徑

train_list =[f for f in os.listdir(train_folder) if f.endswith('.jpg')]
val_list =[f for f in os.listdir(val_folder) if f.endswith('.jpg')]

f_train = open(train_txt_path, 'w')
for i in train_list:
    filename = os.path.join(train_folder, i)
    f_train.write(filename+'\n')
    # print(filename)
f_train.close()

f_val = open(val_txt_path, 'w')
for i in val_list:
    filename = os.path.join(val_folder, i)
    f_val.write(filename+'\n')
    # print(filename)
f_val.close()