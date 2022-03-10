import os

src_dir = input('enter src dir: ')
des_dir = input('enter des dir: ')


count = 1
for f in os.listdir(src_dir):
    pad = 6 - len(str(count))
    name = '0'*pad + str(count) + '.' + f.split('.')[1]

    old_name = os.path.join(src_dir, f)
    new_name = os.path.join(des_dir, name)

    os.rename(old_name, new_name)

    count += 1