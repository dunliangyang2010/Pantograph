import os
import numpy as np

src_dir = input('enter src dir: ')    # 來源路徑
des_dir = input('enter des dir: ')    # 輸出路徑
txt_name = input('train / val: ')    # txt檔名

txt_path = des_dir + '/' + txt_name + '.txt' 

files = os.listdir(src_dir)

txt = open(txt_path, 'w')
for f in files:
    if f.endswith(".jpg"):
        f_name = os.path.join(src_dir, f)
        txt.write(f_name + '\n')
        print(f_name)
txt.close()
