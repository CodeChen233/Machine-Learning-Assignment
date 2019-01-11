import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# import predict
import predict
import numpy as np

class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()

        self.resize(500, 400)
        self.setWindowTitle("人群密度分析")

        self.label = QLabel(self)
        # self.label.setText("   显示图片")
        self.label.setFixedSize(300, 200)
        self.label.move(100, 60)

        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )

        btn = QPushButton(self)
        btn.setText("打开图片")
        btn.move(10, 30)
        btn.clicked.connect(self.openimage)

        self.label2 = QLabel(self)
        self.label2.setText("人群密度分析结果：")
        self.label2.move(10, 280)

        self.label1 = QLabel(self)
        self.label1.setFixedSize(300, 50)
        self.label1.move(100, 300)
        self.label1.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:14px;font-weight:bold;font-family:宋体;}"
                                 )

    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        print(imgName)
        et_count = predict.predict(imgName)
        print(et_count)
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)
        self.label1.setNum(et_count)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())