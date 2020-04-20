参考文章链接：https://www.cnblogs.com/Lazycat1206/p/10256022.html

1. 图像的BGR格式说明

    OpenCV中图像读入的数据格式是numpy的ndarray数据格式。是BGR格式，取值范围是[0,255].

如下图所示，分为三个维度：



第一维度：Height 高度，对应图片的 nRow 行数

第二维度：Width 宽度，对应图片的 nCol 列数

第三维度：Value  代表BGR三通道的值

BGR分别代表蓝色，绿色和红色

2.Image 对象的属性

   image.shape 返回图像的宽度，长度和通道数，如果是灰度图，返回值仅有行数和列数。

   image.size 返回图像的像素

   image.dtype 返回图像的数据类型

1 import cv2
2 import numpy as np
3 img=cv2.imread('buffer.jpg')
4 print("长度:",img.shape[1],  "宽度:",img.shape[0], "通道:", img.shape[2], "像素:", img.size, "数据类型:", img.dtype)
