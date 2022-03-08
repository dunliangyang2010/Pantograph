import cv2
import os

def video_play():
    video = input('video_path:')
    cap = cv2.VideoCapture(video)
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        # frame = cv2.resize(frame, (960, 540))
        cv2.imshow('frame_window', frame)

        key = cv2.waitKey(1) # ESC:27
        if key == 27:
            print('break')
            break
    cap.release()
    cv2.destroyAllWindows()

video_play()
