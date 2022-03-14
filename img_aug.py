import cv2
import os
from imgaug import augmenters as iaa


seq = iaa.Sequential([
    iaa.Crop(px=(1, 5), keep_size=True), # 從每側隨機剪裁圖像1~5px
    # iaa.Fliplr(0.5), # 水平翻轉
    iaa.GaussianBlur(sigma=(1.0, 5.0)), # sigma 1~5 的模糊
    # iaa.Clouds(),
    # iaa.Fog(),
    # iaa.Rain(speed=(0.1, 0.2))
])

src_dir = input('enter src dir: ')
des_dir = input('enter des dir: ')

# test = 'C:\\Windows\\Users\\alexb\\'
# print(repr(test))

file_list = os.listdir(src_dir)

img_list = []
count=0
id = input('enter id head: ')

for i in file_list:
    img_path = src_dir + '\\' + r'{}'.format(i)
    img = cv2.imread(img_path)

    img_list.append( [img])

    images_aug = seq.augment_images(img_list[count]) 

    pad = 6-len(id)
    name = '0'*pad + id
    file_name = des_dir + '\\' + r'{}'.format(name) +'.jpg' # i
    cv2.imwrite(file_name, images_aug[0])
    count += 1
    id = str( int(id) + count )

## ok ########################################################

# count=0
# for i in file_list:
#     img_path = src_dir + '\\' + r'{}'.format(i)
#     img = cv2.imread(img_path)

#     img_list = []
#     img_list.append(img)

#     images_aug = seq.augment_images(img_list) # img_list[count]

#     file_name = des_dir + '\\' + r'{}'.format(i)
#     cv2.imwrite(file_name, images_aug[0])


