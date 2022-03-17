import os
import os.path
import shutil
import random

path = 'image'
num_files = len([f for f in os.listdir(path)
                    if os.path.isfile(os.path.join(path, f))])
# print('training file nums: ', num_files) # 8320


## split data to train and validation
train_ratio = 0.8
train_num = int( round( (num_files)*train_ratio, 0) ) # 6656

images_list = []
for img in os.listdir('image'):
    if img.endswith('.jpg'):
        images_list.append(img.split('.')[0])

random.shuffle(images_list)

### mkdir
if not os.path.isdir('obj'):
  os.mkdir( os.path.join('obj') )

img_folder = os.path.join("image") 
txt_folder = os.path.join("txt")
train_folder = os.path.join("obj/train")
val_folder = os.path.join("obj/val")

if not os.path.isdir("obj/train"):
  os.mkdir(train_folder)    
if not os.path.isdir("obj/val"):
  os.mkdir(val_folder)

print(len(images_list[:train_num]))
print(len(images_list[train_num:]))

# train data 
for train_data in images_list[:train_num]:
  shutil.copyfile(os.path.join(img_folder, "{}.jpg".format(train_data)),  
          os.path.join(train_folder, "{}.jpg".format(train_data)))
  shutil.copyfile(os.path.join(txt_folder, "{}.txt".format(train_data)),  
          os.path.join(train_folder, "{}.txt".format(train_data)))
   
# val data
for test_data in images_list[train_num:]:
  shutil.copyfile(os.path.join(img_folder, "{}.jpg".format(test_data)),  
          os.path.join(val_folder, "{}.jpg".format(test_data)))
  shutil.copyfile(os.path.join(txt_folder, "{}.txt".format(test_data)),  
          os.path.join(val_folder, "{}.txt".format(test_data)))
# show total data 
print("="*35)
print("number of training set :", len(os.listdir(train_folder))) # image+txt: 6656*2
print("number of validation set :", len(os.listdir(val_folder))) # image+txt: 1663*2
print("="*35)
