import cv2
import os

img_dir = input('img_dir:')
size = (1200, 1200) # 需與轉換圖片一致!!
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

video_writer = cv2.VideoWriter(r'D:\openCV\spark\output.mp4', fourcc, 2.0, size)
img_array = []

for img in os.listdir(img_dir):
    img_path = img_dir + '\\' + img
    
    image = cv2.imread(img_path)
    if image is None:
        print('Image is None')
        continue

    img_array.append(image)

for i in range( len(img_array)):
    video_writer.write(img_array[i])

print('done!')

###########################################################################
# import numpy as np
# import cv2

# size = (640,360) # 1200, 1200
# print(size)
# #完成寫入物件的建立，第一個引數是合成之後的影片的名稱，第二個引數是可以使用的編碼器，第三個引數是幀率即每秒鐘展示多少張圖片，第四個引數是圖片大小資訊
# videowrite = cv2.VideoWriter(r'D:\openCV\spark\output.mp4',-1,1,size)#20是幀數，size是圖片尺寸
# img_array=[]
# for filename in [r'D:\openCV\spark\testfig\{0}.jpg'.format(i) for i in range(200)]:
#     img = cv2.imread(filename)
#     if img is None:
#         print(filename + " is error!")
#         continue
#     img_array.append(img)
# for i in range(200):
#     videowrite.write(img_array[i])
# print('end!')

###########################################################################

# cv2.VideoWriter() 的第一個參數是指定輸出的檔名，例如：下列範例中的 output.avi，
# 第二個參數為指定 FourCC，
# 第三個參數為 fps 影像偵率，
# 第四個參數為 frameSize 影像大小，
# 最後參數代表是否要存彩色，否則就存灰階，預設為 true，

# import cv2

# img_path = input('img_path:')
# cap = cv2.VideoCapture(img_path)

# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'MP4V') # FourCC 是 4-byte 大小的碼，用來指定影像編碼方式
# out = cv2.VideoWriter('output.mp4', fourcc, 2.0, (640,  360))
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # 水平上下翻轉影像
#     #frame = cv2.flip(frame, 0)
#     # write the flipped frame
#     out.write(frame)
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) == 27:
#         print('break')
#         break
# # Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()








