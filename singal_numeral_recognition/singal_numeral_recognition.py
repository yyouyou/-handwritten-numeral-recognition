from PIL import Image
import PIL.ImageOps
import os
import numpy

width = 50
total = 1000
size = 15
w_rate = 0.1

#在一张大的图片中选取有字的部分
def find_count(im):
    seq = list(im.getdata())
    for x1 in range(0, im.size[0]-1 + 1):
        num = 0
        for y in range(0, im.size[1]-1 + 1):
            num = num + seq[y*im.size[0]+x1-1]
        if num != 0:
            break
    if x1 == im.size[0]-1:
        return 0
    else:
        x2 = im.size[0]-1
        while x2 >= x1:
            num = 0
            for y in range(0, im.size[1]-1 + 1):
                num = num + seq[y*im.size[0]+x2-1]
            if num != 0:
                break
            x2 = x2-1
    for y1 in range(0, im.size[1] + 1):
        num = 0
        for x in range(0, im.size[0]-1 + 1):
            num = num+seq[y1*im.size[0]+x-1]
        if num != 0:
            break
    if y1 == im.size[1]:
        return 0
    else:
        y2 = im.size[1]-1
        while y2 >= y1:
            num = 0
            for x in range(0, im.size[0]-1 + 1):
                num = num + seq[y2* im.size[0]+x-1]
            if num != 0:
                break
            y2 = y2 - 1
    #print(y1, x1, y2, x2)
    im1 = im.crop((x1, y1, x2, y2))
    im1.save("after_cut.jpg")
    return im1

#判断一张切割后的图片块是否为白色
def judge_white(im):
    seq = list(im.getdata())
    n = 0
    for i in range(0, len(seq)-1 + 1):
        n = n+seq[i]/255
    #print(seq)
    #print(n)
    if(n>=len(seq)*w_rate):
        #print(1)
        return 1
    else:
        return 0

#缩小图片
def reduce_pictures(im):
    a = numpy.zeros((size, size))
    dx = im.size[0]/size
    dy = im.size[1]/size
    n = 1

    x1 = 0
    y1 = 0
    x2 = dx
    y2 = dy

    while y2 <= im.size[1]-1:
        x1 = 0
        x2 = dx
        while x2 <= im.size[0]-1:
            im1 = im.crop((x1, y1, x2, y2))
           # print(str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2))
            if judge_white(im1)==1:
                a[int(x2/dx)][int(y2/dy)] = 1
            x1 = x1+dx
            x2 = x2+dx
            n = n+1
        y1 = y1+dy
        y2 = y2+dy
    return a

def adjust_c(im):
    seq = list(im.getdata())


#将图片其规范化
def adjust(name):
    try:
        im = Image.open(name)
    except IOError:
        print("Cannot open")
        return 0
    # 反转颜色
    im = PIL.ImageOps.invert(im)
    im1 = im.convert("L")
    #im1 = im.convert("1")
    im2 = find_count(im1)
    if im2.size[0]<=4*size or im2.size[1]<=4*size:
        im2 = im2.resize((im2.size[0] * size, im2.size[1] * size))
    mtr = reduce_pictures(im2)
    return mtr


#sigmoid函数
def sigmoid(param):
    return 1 / (1 + numpy.e**( -param ))

#从文件中获取权值数据
def get_output(test1_data):
    test1_w1 = numpy.loadtxt("weight15501.txt")
    test1_w2 = numpy.loadtxt("weight15502.txt")

    test1_input = test1_data.reshape((1,size*size))

    test1_hide = numpy.dot(test1_input, test1_w1)
    test1_output = sigmoid(numpy.dot(sigmoid(test1_hide), test1_w2))
    return test1_output

#得到输出的y的最大值
def MAX(test1_output,i):
    max1= 0
    for j in range(10):
        if test1_output[i][j]>=test1_output[i][max1]:
            max1= j
    print(str(test1_output))
    return max1

#print(adjust("test.jpg"))
print(MAX(get_output(adjust("test.jpg")),0))