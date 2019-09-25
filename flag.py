# -*- coding: utf-8 -*-
from PIL import Image
#读取图片
flag = Image.open("C:\\Users\\lenovo\\Desktop\\flag.png")
head = Image.open("C:\\Users\\lenovo\\Desktop\\head.jpg")
#计算缩放比例
ratio = head.width/flag.width/4
size = (int(flag.width*ratio),int(flag.height*ratio))
#缩放国企图片
flag = flag.resize(size,Image.ANTIALIAS)
#计算坐标
position = (head.width-flag.width,head.height-flag.height)
#合成图片并保存
head.paste(flag,position)
head.save("C:\\Users\\lenovo\\Desktop\\head_flag.jpg","jpeg")