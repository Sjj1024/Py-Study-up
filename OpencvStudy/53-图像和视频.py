import cv2 as cv


def get_video():
    print("读取视频的方法")
    # 使用视频捕获的方法，捕获传递进来的视频名称
    video = cv.VideoCapture("video1.mp4")
    while (True):
        # 读取到的视频返回两个值，一个真假，一个帧，也就是一个图片
        ret, frame = video.read()
        print(ret, frame)
        # flip是反转，将视频反转180度
        new_flime = cv.flip(frame, 1)
        # 因为opencv是做图像处理的，所以读取出来的视频是没有声音的
        cv.imshow("video", frame)
        c = cv.waitKey(50)
        if c == 27:
            break


def get_pixels():
    img = cv.imread("2.jpg")
    # img = cv.imread("cat.jpg")
    print(img.shape)
    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]
    print(f"图像的宽：{height} 高：{width} 色彩通道：{channels}")
    for h in range(height):
        for w in range(width):
            for c in range(channels):
                # 获取到每个像素点的值
                pv = img[h, w, c]
                # 然后将像素点所有颜色翻转后，重新赋值
                img[h, w, c] = 255 - pv
    cv.imshow("new", img)
    cv.waitKey(0)


if __name__ == '__main__':
    # get_video()
    get_pixels()
