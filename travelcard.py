# coding=UTF-8
from PIL import Image,ImageDraw
import time
# 一定要从微信小程序通信行程卡截图！
# 手动把要替换的位置找到，左，上，右，下
def newcard(sour,dest):
    (left,upper,right,down)=(410,702,873,745)
    s=time.strftime("%Yd%md%ds%Hm%Mm%S",time.localtime(time.time()-30))
    im_time = Image.new("RGB",(462,42),(255,255,255))
    current_place=0
    for name in list(s):
        current_im=Image.open(name+'.png')
        im_time.paste(current_im,(current_place,0))
        current_place+=current_im.getbbox()[2]
    t=im_time.resize((right-left,down-upper))
    im=Image.open(sour)
    dr=ImageDraw.Draw(im)
    dr.rectangle((left-3,upper-3,right+3,down+3),fill=(255,255,255))
    im.paste(t,(left,upper))
    im.save(dest)

if __name__ == "__main__":
    newcard('xcko.jpg','xck.jpg')