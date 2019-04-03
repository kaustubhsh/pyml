from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import cv2

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150,150,350,500)
        self.setWindowTitle("Instagram effects")
        self.ui()

    def ui(self):
        main_layout = QVBoxLayout()
        # main_layout.addStretch(1)

        effect_list = ['none', 'b/w', 'blur', 'negative']
        grid = QGridLayout()
        k=0
        for i in range(2):
            for j in range(2): # range(len(effect_list)/2)
                button = QPushButton(effect_list[k])
                button.clicked.connect(self.applyEffect)
                grid.addWidget(button, i, j)
                k=k+1

        
        # for video processing >>>
        self.image_label = QLabel(self)
        self.org_pic = cv2.imread('Penguins.jpg')
        self.org_pic = cv2.resize(self.org_pic,(400,300))
        self.display(self.org_pic)    
        # end video processing <<<
        
    
        '''
        # for image processing >>>
        image_label = QLabel(self)
        pixmap = QPixmap('perspective_image.png')
        image_label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        # end image processing <<<
        '''

        main_layout.addWidget(self.image_label)
        main_layout.addLayout(grid)
        self.setLayout(main_layout)


    def applyEffect(self):
        btn = self.sender()
        print(btn.text())

        if btn.text() == 'none':
            self.display(self.org_pic)
        if btn.text() == 'b/w':
            gray_pic = cv2.cvtColor(self.org_pic, cv2.COLOR_BGR2GRAY)
            gray_pic = cv2.cvtColor(gray_pic, cv2.COLOR_GRAY2BGR)
            self.display(gray_pic)
            '''
            bpc = 1 if gray_pic.ndim == 2 else gray_pic.shape[2]
            ### strides = bpc*width
            '''
            '''
            height, width = gray_pic.shape[:2]
            image = QImage(gray_pic.data, width, height, gray_pic.strides[0], QImage.Format_RGB888)
            pixMap = QPixmap(image)
            self.image_label.setPixmap(pixMap)
            # self.resize(width, height)
            '''


    def display(self, picture):
        # picture = cv2.resize(picture,(400,300))
        height, width, bpc = picture.shape
        image = QImage(picture.data, width, height, bpc*width, QImage.Format_RGB888)
        pixMap = QPixmap(image)
        self.image_label.setPixmap(pixMap)
        # self.resize(width, height)
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())