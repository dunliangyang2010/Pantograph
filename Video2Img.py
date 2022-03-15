import cv2
import os

def video_to_frames():
    video = input('video_path:')
    output_path = input('output_path:')

    cap = cv2.VideoCapture(video)
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(os.path.join(output_path, '%d.jpg') % count, frame)
            count += 1

            # key = cv2.waitKey(1)
            # if key == 27:
            #     print('break')
            #     break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    video_to_frames()
