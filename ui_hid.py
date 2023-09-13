import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout, QPushButton, QTextEdit, QLabel, \
    QGridLayout, QMainWindow, QAction, QWidgetAction, QSizePolicy


class MyWidget(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)
        self.icon_init()
        self.combobox_init()
        self.toolbar_init()
        self.text_input()
        self.text_output()
        self.status_label_init()
        self.hid_info_box_init()

        self.init_ui()

    def init_ui(self):

        # 设置hid窗口
        self.hid_widget = QWidget()

        self.setWindowIcon(QIcon("./icon/win.png"))
        self.hid_widget.setStyleSheet("background-color:#D0BFFF")
        self.setCentralWidget(self.hid_widget)
        self.resize(800, 600)
        # 设置菜单栏
        menubar = self.menuBar()
        about_menu = menubar.addMenu("关于")
        help_menu = menubar.addMenu("帮助")

        # 二级菜单
        about_menu.addAction("hange")

        # 设置状态栏
        self.status = self.statusBar()
        self.status.showMessage("作者：hange")

        # 窗口主布局
        grid = QGridLayout()
        self.hid_widget.setLayout(grid)

        layout_right = QVBoxLayout()
        layout_left = QVBoxLayout()
        layout_left_top = QVBoxLayout()
        layout_left_bottom = QVBoxLayout()

        layout_text = QVBoxLayout()

        # self.move(500, 200)
        self.setLayout(grid)
        grid.addLayout(layout_left, 0, 0)

        grid.addLayout(layout_right, 0, 1)
        # 设置延展
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 2)

        # layout_right
        layout_right.addLayout(layout_text)
        # layout_left
        layout_left.addLayout(layout_left_top)
        layout_left.addLayout(layout_left_bottom)
        # layout_left_top
        layout_left_top.addWidget(self.combobox)
        layout_left_top.addWidget(self.status_label)
        # 设置页边距（左、上、右、下）
        layout_left_top.setContentsMargins(10, 0, 30, 0)

        layout_left_bottom.addWidget(self.pid_label)
        layout_left_bottom.addWidget(self.vid_label)
        layout_left_bottom.addWidget(self.Manufacturer_label)
        layout_left_bottom.addWidget(self.Serial_label)

        layout_text.addWidget(self.edit_input)

         # 设置间隔的宽度

        layout_text.setSpacing(40)

        layout_text.addWidget(self.edit_output)
        layout_text.addStretch(1)

        layout_text.setContentsMargins(10, 0, 10, 10)
        # 在layout_left_top中添加伸展因子
        layout_left_top.addStretch(1)
        # 在layout_left_bottom中添加伸展因子
        layout_left_bottom.addStretch(1)

    def icon_init(self):
        self.connect_icon = QtGui.QIcon()
        self.send_icon = QtGui.QIcon()
        self.refresh_icon = QtGui.QIcon()

        self.connect_icon.addPixmap(QtGui.QPixmap("./icon/connect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.connect_icon.addPixmap(QtGui.QPixmap("./icon/unconnect.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.refresh_icon.addPixmap(QtGui.QPixmap("./icon/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_icon.addPixmap(QtGui.QPixmap("./icon/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    # hid_info_box.addWidget(self.pid_label)
    def toolbar_init(self):
        # 工具栏

        self.toolbar = self.addToolBar("toolbar")
        # 设置高度
        self.toolbar.setFixedHeight(60)

        self.toolbar.setStyleSheet("QToolBar{spacing:10px;background-color:#DFCCFB}")
        # 创建连接按钮
        self.connect_button = QPushButton(QIcon("./icon/connect.png"), "")
        self.connect_button.setIconSize(QSize(48, 48))  # 设置图标大小

        # 设置按钮的不同状态的图标
        self.connect_button.setIcon(self.connect_icon)  # 正常状态
        self.connect_button.setCheckable(True)  # 设置按钮为可选中状态
        self.connect_button.setFlat(1)

        self.send_button = QPushButton(QIcon("./icon/send.png"), "")
        self.send_button.setIconSize(QSize(48, 48))  # 设置图标大小
        self.send_button.setFlat(1)

        self.refresh_button = QPushButton(QIcon("./icon/refresh.png"), "")
        self.refresh_button.setIconSize(QSize(48, 48))
        self.refresh_button.setFlat(1)

        self.toolbar.addWidget(self.connect_button)

        self.toolbar.addWidget(self.send_button)
        self.toolbar.addWidget(self.refresh_button)

    def combobox_init(self):
        self.combobox = QComboBox(self)
        self.combobox.setStyleSheet("color: #862B0D;font-size: 20px;font-family: 'Times New Roman';background-color: #DFCCFB;")
        self.combobox.setFixedSize(250, 30)
    def status_label_init(self):
        self.status_label=QLabel(self)
        self.status_label.setStyleSheet("color: #862B0D;font-size: 20px;font-family: 'Times New Roman';")



    def text_input(self):
        self.edit_input = QTextEdit(self)
        self.edit_input.setPlainText("请输入要发送的内容")
        self.edit_input.setStyleSheet("color: #862B0D;font-size: 20px;font-family: '楷体';background-color: #DFCCFB;border: 2px solid #D0BFFF")
        self.edit_input.setFixedHeight(300)  # 设置输入框的高度为150像素

    def text_output(self):
        self.edit_output = QTextEdit(self)
        self.edit_output.setPlainText("接收的内容")
        self.edit_output.setStyleSheet("color: #862B0D;font-size: 20px;font-family: '楷体';background-color: #DFCCFB;border: 2px solid #D0BFFF;")
        self.edit_output.setFixedHeight(200)  # 设置输入框的高度为150像素

    def text_contain(self):
        pass

    def hid_info_box_init(self):
        self.pid_label = QLabel(self)
        self.pid_label.setText("PID:")
        self.pid_label.setStyleSheet ("color: #862B0D;font-size: 20px;font-family: 'Times New Roman';")
        self.pid_label.setFixedHeight(20)  # 设置高度为20像素

        self.vid_label = QLabel(self)
        self.vid_label.setText("VID:")
        self.vid_label.setStyleSheet("color: #862B0D;font-size: 20px;font-family: 'Times New Roman';")
        self.vid_label.setFixedHeight(20)  # 设置高度为20像素

        self.Manufacturer_label = QLabel(self)
        self.Manufacturer_label.setText("Manufacturer:")
        self.Manufacturer_label.setStyleSheet("color: #862B0D;font-size: 20px;font-family: 'Times New Roman';")
        self.Manufacturer_label.setFixedHeight(20)  # 设置高度为20像素



        self.Serial_label = QLabel(self)
        self.Serial_label.setText("Serial NO:")
        self.Serial_label.setStyleSheet("color: #862B0D;font-size: 20px;font-family: 'Times New Roman';")
        self.Serial_label.setFixedHeight(20)  # 设置高度为20像素



# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     my_widget = MyWidget("hid")
#     my_widget.show()
#     sys.exit(app.exec_())
