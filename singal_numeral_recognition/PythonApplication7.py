import sys
from PyQt5.QtWidgets import (QApplication, QWidget,QTextBrowser, QLabel, QGridLayout, QTextEdit, QLineEdit,QPushButton)
from PyQt5.QtGui import (QPainter, QPen,QFont,QPalette,QColor)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5 import QtCore
import single as x
import string
from PIL import Image
import PIL.ImageOps
import os
import numpy
import network as net

class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()

        #resize设置宽高，move设置位置
        self.resize(800, 400)
        #self.move(100, 100)
        self.setWindowTitle("手写数字识别")
        self.setFixedSize(self.width(), self.height())
        #setMouseTracking设置为False，否则不按下鼠标时也会跟踪鼠标事件
        self.setMouseTracking(False)
        palette1 = QPalette()
        palette1.setColor(self.backgroundRole(), QColor(255,255,255))   # 设置背景颜色
        self.setPalette(palette1)

        self.button0=QPushButton(self)
        self.button0.setText("0")
        self.button0.move(310,20)
        self.button1=QPushButton(self)
        self.button1.setText("1")
        self.button1.move(450,20)
        self.button2=QPushButton(self)
        self.button2.setText("2")
        self.button2.move(590,20)
        self.button3=QPushButton(self)
        self.button3.setText("3")
        self.button3.move(310,60)
        self.button4=QPushButton(self)
        self.button4.setText("4")
        self.button4.move(450,60)
        self.button5=QPushButton(self)
        self.button5.setText("5")
        self.button5.move(590,60)
        self.button6=QPushButton(self)
        self.button6.setText("6")
        self.button6.move(310,100)
        self.button7=QPushButton(self)
        self.button7.setText("7")
        self.button7.move(450,100)
        self.button8=QPushButton(self)
        self.button8.setText("8")
        self.button8.move(590,100)
        self.button9=QPushButton(self)
        self.button9.setText("9")
        self.button9.move(310,140)
        self.button0.clicked.connect(self.button0clicked)
        self.button1.clicked.connect(self.button1clicked)
        self.button2.clicked.connect(self.button2clicked)
        self.button3.clicked.connect(self.button3clicked)
        self.button4.clicked.connect(self.button4clicked)
        self.button5.clicked.connect(self.button5clicked)
        self.button6.clicked.connect(self.button6clicked)
        self.button7.clicked.connect(self.button7clicked)
        self.button8.clicked.connect(self.button8clicked)
        self.button9.clicked.connect(self.button9clicked)

        self.edit=QTextBrowser(self)#创建显示文本框
        self.edit.resize(400,120)
        self.edit.move(350,250)
        self.edit.append("begin")
        #pe=QPalette()#设置文字颜色
        #pe.setColor(QPalette.Text,Qt.red)
        #self.edit.setPalette(pe)
        self.edit.setFont(QFont( "Timers",20,QFont.Bold))
        la=QLabel(self)#显示要求
        la.move(320,180)
        la.setText('请在左侧方框内手写数字')
        la.setFont(QFont( "Timers",17,QFont.Bold))

        self.Button1 = QPushButton(self)#确认按键
        self.Button1.setText("Ok")
        self.Button1.move(180,320)
        self.Button2 = QPushButton(self)#清除按键
        self.Button2.setText("Clear")
        self.Button2.move(50,320)
        self.Button1.clicked.connect(self.btn1clicked)#截图识别函数
        self.Button2.clicked.connect(self.btn2clicked)#清除函数
        self.pos_xy = []#保存轨迹
    
    def button0clicked(self):
        input=x.adjust("test.jpg").reshape((1,net.IN_NUM))
        temp=[1,0,0,0,0,0,0,0,0,0]
        inputs=list(input[0])
        inputs.extend(temp)
        n=net.neuralnetwork(net.IN_NUM,net.HIDE_NUM,net.OUT_NUM)
        n.train(inputs,net.MIU,net.FOR_TIMES,net.ERRON_CHANGE)
        self.edit.append("ok!!")

    def button1clicked(self):
        input=x.adjust("test.jpg").reshape((1,net.IN_NUM))
        temp=[0,1,0,0,0,0,0,0,0,0]
        inputs=list(input[0])
        inputs.extend(temp)
        n=net.neuralnetwork(net.IN_NUM,net.HIDE_NUM,net.OUT_NUM)
        n.train(inputs,net.MIU,net.FOR_TIMES,net.ERRON_CHANGE)
        self.edit.append("ok!!")

    def button2clicked(self):
        input=x.adjust("test.jpg").reshape((1,net.IN_NUM))
        temp=[0,0,1,0,0,0,0,0,0,0]
        inputs=list(input[0])
        inputs.extend(temp)
        n=net.neuralnetwork(net.IN_NUM,net.HIDE_NUM,net.OUT_NUM)
        n.train(inputs,net.MIU,net.FOR_TIMES,net.ERRON_CHANGE)
        self.edit.append("ok!!")


    def button3clicked(self):
        input=x.adjust("test.jpg").reshape((1,net.IN_NUM))
        temp=[0,0,0,1,0,0,0,0,0,0]
        inputs=list(input[0])
        inputs.extend(temp)
        n=net.neuralnetwork(net.IN_NUM,net.HIDE_NUM,net.OUT_NUM)
        n.train(inputs,net.MIU,net.FOR_TIMES,net.ERRON_CHANGE)
        self.edit.append("ok!!")

    def button4clicked(self):
        input=x.adjust("test.jpg").reshape((1,net.IN_NUM))
        temp=[0,0,0,0,1,0,0,0,0,0]
        inputs=list(input[0])
        inputs.extend(temp)
        n=net.neuralnetwork(net.IN_NUM,net.HIDE_NUM,net.OUT_NUM)
        n.train(inputs,net.MIU,net.FOR_TIMES,net.ERRON_CHANGE)
        self.edit.append("ok!!")

    def button5clicked(self):
        input=x.adjust("test.jpg").reshape((1,net.IN_NUM))
        temp=[0,0,0,0,0,1,0,0,0,0]
        inputs=list(input[0])
        inputs.extend(temp)
        n=net.neuralnetwork(net.IN_NUM,net.HIDE_NUM,net.OUT_NUM)
        n.train(inputs,net.MIU,net.FOR_TIMES,net.ERRON_CHANGE)
        self.edit.append("ok!!")

    def button6clicked(self):
        input=x.adjust("test.jpg").reshape((1,net.IN_NUM))
        temp=[0,0,0,0,0,0,1,0,0,0]
        inputs=list(input[0])
        inputs.extend(temp)
        n=net.neuralnetwork(net.IN_NUM,net.HIDE_NUM,net.OUT_NUM)
        n.train(inputs,net.MIU,net.FOR_TIMES,net.ERRON_CHANGE)
        self.edit.append("ok!!")

    def button7clicked(self):
        input=x.adjust("test.jpg").reshape((1,net.IN_NUM))
        temp=[0,0,0,0,0,0,0,1,0,0]
        inputs=list(input[0])
        inputs.extend(temp)
        n=net.neuralnetwork(net.IN_NUM,net.HIDE_NUM,net.OUT_NUM)
        n.train(inputs,net.MIU,net.FOR_TIMES,net.ERRON_CHANGE)
        self.edit.append("ok!!")

    def button8clicked(self):
        input=x.adjust("test.jpg").reshape((1,net.IN_NUM))
        temp=[0,0,0,0,0,0,0,0,1,0]
        inputs=list(input[0])
        inputs.extend(temp)
        n=net.neuralnetwork(net.IN_NUM,net.HIDE_NUM,net.OUT_NUM)
        n.train(inputs,net.MIU,net.FOR_TIMES,net.ERRON_CHANGE)
        self.edit.append("ok!!")

    def button9clicked(self):
        input=x.adjust("test.jpg").reshape((1,net.IN_NUM))
        temp=[0,0,0,0,0,0,0,0,0,1]
        inputs=list(input[0])
        inputs.extend(temp)
        n=net.neuralnetwork(net.IN_NUM,net.HIDE_NUM,net.OUT_NUM)
        n.train(inputs,net.MIU,net.FOR_TIMES,net.ERRON_CHANGE)
        self.edit.append("ok!!")

    def btn2clicked(self):
        self.pos_xy=[]
        self.update()

    def btn1clicked(self):
        id=self.winId()
        self.originalPixmap =QtGui.QGuiApplication.primaryScreen().grabWindow(id,5,5,295,295)  # 获取 屏幕桌面截图
        self.originalPixmap.save("test.jpg", "jpg")
        text_name=x.MAX(x.get_output(x.adjust("test.jpg")),0)
        if text_name<=9:
            self.edit.append(str(text_name))
        else :
            self.edit.append("reject.")

    def paintEvent(self, event):#画图函数
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.black,10, Qt.SolidLine)
        painter.drawRect(0,0,300,300)
        painter.setPen(pen)

        '''
            首先判断pos_xy列表中是不是至少有两个点了
            然后将pos_xy中第一个点赋值给point_start
            利用中间变量pos_tmp遍历整个pos_xy列表
                point_end = pos_tmp

                判断point_end是否是断点，如果是
                    point_start赋值为断点
                    continue
                判断point_start是否是断点，如果是
                    point_start赋值为point_end
                    continue

                画point_start到point_end之间的线
                point_start = point_end
            这样，不断地将相邻两个点之间画线，就能留下鼠标移动轨迹了
        '''
        if len(self.pos_xy) > 1:
            point_start = self.pos_xy[0]
            for pos_tmp in self.pos_xy:
                point_end = pos_tmp

                if point_end == (-1, -1):
                    point_start = (-1, -1)
                    continue
                if point_start == (-1, -1):
                    point_start = point_end
                    continue

                painter.drawLine(point_start[0], point_start[1], point_end[0], point_end[1])
                point_start = point_end
        painter.end()

    def mouseMoveEvent(self, event):
        '''
            按住鼠标移动事件：将当前点添加到pos_xy列表中
            调用update()函数在这里相当于调用paintEvent()函数
            每次update()时，之前调用的paintEvent()留下的痕迹都会清空
        '''
        #中间变量pos_tmp提取当前点
        if (event.pos().x()<=300 and event.pos().y()<=300):
            pos_tmp = (event.pos().x(), event.pos().y())
        #pos_tmp添加到self.pos_xy中
            self.pos_xy.append(pos_tmp)
        else :
            pos_test = (-1, -1)
            self.pos_xy.append(pos_test)

        self.update()

    def mouseReleaseEvent(self, event):
        '''
            重写鼠标按住后松开的事件
            在每次松开后向pos_xy列表中添加一个断点(-1, -1)
            然后在绘画时判断一下是不是断点就行了
            是断点的话就跳过去，不与之前的连续
        '''
        pos_test = (-1, -1)
        self.pos_xy.append(pos_test)
        self.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    handwrite_number= Example()
    handwrite_number.show()
    app.exec_()