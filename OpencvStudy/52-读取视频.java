import cv2 as cv


def get_video():
    print("读取视频的方法")
    video = cv.VideoCapture("video1.mp4")
    while (True):
        ret, frame = video.read()
        print(ret, frame)
        # flip是反转，将视频反转180度
        new_flime = cv.flip(frame, 1)
        # 因为opencv是做图像处理的，所以读取出来的视频是没有声音的
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break


if __name__ == '__main__':
    get_video()
