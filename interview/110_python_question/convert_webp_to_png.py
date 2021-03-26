from io import BytesIO
from PIL import Image  # 注意我的Image版本是pip3 install Pillow==4.3.0

import sys
import io


def covert(fname):
    with open(fname, 'rb') as fp:
        byte_stream = BytesIO(fp.read())

    roiImg = Image.open(byte_stream)   # Image打开Byte字节流数据
    # roiImg.show()   #  弹出 显示图片
    imgByteArr = io.BytesIO()     # 创建一个空的Bytes对象

    roiImg.save(imgByteArr, format='PNG') # PNG就是图片格式，我试过换成JPG/jpg都不行

    imgByteArr = imgByteArr.getvalue()   # 这个就是保存的图片字节流

    # 下面这一步只是本地测试， 可以直接把imgByteArr，当成参数上传到七牛云
    with open("./%s.png" % fname, "wb") as f:
        f.write(imgByteArr)

import os
for i in range(0, 87):
    #covert(str(i))

    os.remove(str(i))




