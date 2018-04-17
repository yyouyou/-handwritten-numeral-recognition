from PIL import Image
import PIL.ImageOps
import os
import numpy
#切割单张图片x*y个
def cut(x,y,id,name):
    name1 = name+str(id)+".jpg"
    name1 = "E:\\python\\pictures\\"+name+str(id)+".jpg"
    im = Image.open(name1)

    #偏移量
    dx = im.size[0]/x
    dy = im.size[1]/y
    n = 0

    dx = 28
    dy = 28
    x1 = 0
    y1 = 0
    x2 = dx
    y2 = dy

    while y2 <= im.size[1] and n <= 500:
        x1 = 0
        x2 = dx
        while x2 <= im.size[0]:
            name2 = "E:\\python\\pictures\\"+str(id)+"\\"+str(n)+".jpg"
            im1 = im.crop((x1,y1,x2,y2))
            im1.save(name2)
            x1 = x1+dx
            x2 = x2+dx
            n = n+1
            if n >= 500:
                break
        y1 = y1+dy
        y2 = y2+dy


    #print(str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2))
    print("图片切割成功")
    return n

#将一组图片切割
def allcut(name):
    x = 10
    y = 2
    for i in range(0,9 + 1):
        cut(x, y, i, name)
    return x*y

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
                #print(x2)
                #print(y)
                num = num + seq[y*im.size[0]+x2-1]
            #print(x2*im.size[0]+y-1)
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
    print(y1, x1, y2, x2)
    im1 = im.crop((x1, y1, x2, y2))
    #im1.save("test.jpg")
    return im1

#判断一张图片是否为白色
def judge_white(im,rate):
    seq = list(im.getdata())
    n = 0
    for i in range(0, len(seq)-1 + 1):
        n = n+seq[i]/255
    if(n>=len(seq)*rate):
        return 1
    else:
        return 0

#缩小图片
def reduce_pictures(size,im,rate):
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
            if judge_white(im1,rate)==1:
                a[int(x2/dx)][int(y2/dy)] = 1
            x1 = x1+dx
            x2 = x2+dx
            n = n+1
        y1 = y1+dy
        y2 = y2+dy
        #print(n)
    return a

#将图片其规范化
def adjust(size, name):
    try:
        im = Image.open(name)
    except IOError:
        print("Cannot open")
        return 0
    im = PIL.ImageOps.invert(im)
    im1 = im.convert("1")
    im2 = find_count(im1)
    im2 = im2.resize((im2.size[0]*10,im2.size[1]*10))
    mtr = reduce_pictures(size, im2, 0.1)
    return mtr

#将图片规范化的矩阵输入到文件中
def infile_input_number(mtr,num,name):
    a = numpy.zeros((10))
    a[num] = 1
   # mtr = numpy.array(mtr, dtype='int32')
    a = numpy.array(a)
    fp = open(name, 'a+')

    #print(str(mtr)+"33333333\n")
    for i in range(0, mtr.shape[0]-1 + 1):
        for j in range(0, mtr.shape[1]-1 +1):
            fp.write(str(mtr[i][j])+" ")
    for i in range(0, 10, + 1):
        fp.write(str(a[i])+" ")
    fp.write("\n")
    fp.close()
    #mtr1 = numpy.loadtxt(name)
    #print(mtr1)
    #print(mtr)

#将所有图片规范化的矩阵输入到文件中
def allinfile(num,size,name):
        for j in range(501, num + 1):
            i = 1
        #for i in range(0, 9 + 1):
            #print(i)
            print(j)
            infile_input_number(adjust(size,"E:\\python\\pictures\\"+str(i)+"\\"+str(j)+".jpg"), i, "train10.txt")
            #infile_input_number(adjust(10, name + str(i) + str(j) + ".jpg"), i,
                               # "train1.txt")


def inverted(name):
    # 读入图片
    image = Image.open(name+".png")

    # 反转颜色
    inverted_image = PIL.ImageOps.invert(image)

    # 保存图片
    inverted_image.save(name+"_inverted.jpg")
    return inverted_image

#将png图片格式转为jpg格式
def change_jpg(name):
    for i in range(10):
        for j in range(5):
            try:
                im = Image.open(name+str(i)+str(j)+".png")
            except IOError:
                print("Cannot open")
                return 0
            im1 = im.convert("1")
            im1.save(name+str(i)+str(j)+".jpg")


#inverted("666")
allinfile(510,10,"E:\\python\\DigitalRecognition1\\numebr\\")
#print(numpy.loadtxt("train15.txt").shape)
#allinfile(7,10,"")
#inputmtr=numpy.loadtxt("train.txt")
#print(inputmtr.shape)
#infile_input_number(adjust(10, "000.png"),0, "000.txt")
#allcut("test1")
#print(adjust(10, "train11.jpg"))
#change_jpg("")
#print(numpy.loadtxt("train1.txt").shape)
#allcut("mnist_train")
#adjust(10,"E:\\python\\pictures\\"+'5'+"\\"+'0'+".jpg")