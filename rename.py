import os

src_dir = input('enter src dir: ')
des_dir = input('enter des dir: ')
files = os.listdir(src_dir)

for f in files:
    padding = 6-len(f.split('.')[0])
    # new_name = "0"*padding + f 

    old_name = os.path.join(src_dir, f)
    new_name = os.path.join(des_dir, "0"*padding + f )
    os.rename(old_name, new_name)