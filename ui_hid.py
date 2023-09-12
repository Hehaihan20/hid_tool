from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QComboBox, QVBoxLayout, QPushButton, QTextEdit, QLabel, \
    QGridLayout
import sys


class MyWidget(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.combobox_init()
        self.button_init()
        self.text_input()
        self.text_output()
        self.hid_info_box_init()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        layout_right = QVBoxLayout()
        layout_left=QVBoxLayout()
        layout_left_top = QVBoxLayout()
        layout_left_bottom = QVBoxLayout()

        layout_text = QVBoxLayout()
        self.resize(800, 600)
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
        layout_left_top.addWidget(self.btn_open)
        # 设置页边距（左、上、右、下）
        layout_left_top.setContentsMargins(10, 0, 0, 0)
        #控件间距
        layout_left_top.setSpacing(20)
        layout_left_top.setAlignment(self.btn_open, Qt.AlignRight)

        layout_left_bottom.addWidget(self.pid_label)
        layout_left_bottom.addWidget(self.vid_label)
        layout_text.addWidget(self.edit_input)
        layout_text.addWidget(self.btn_send)
        layout_text.addWidget(self.edit_output)
        layout_text.setAlignment(self.btn_send, Qt.AlignRight)

        # 在layout_left_top中添加伸展因子
        layout_left_top.addStretch(1)
        # 在layout_left_bottom中添加伸展因子
        layout_left_bottom.addStretch(1)
       # hid_info_box.addWidget(self.pid_label)

    def combobox_init(self):
        self.combobox = QComboBox(self)
        self.combobox.setFixedSize(250, 40)

        self.combobox.currentIndexChanged.connect(self.print_device_info)

    def button_init(self):
        self.btn_open = QPushButton("打开端口")
        self.btn_open.setFixedSize(80, 40)
        self.btn_open.setParent(self)

        self.btn_send = QPushButton("发送")
        self.btn_send.setParent(self)
        self.btn_send.setFixedSize(100, 40)

    def text_input(self):
        self.edit_input = QTextEdit(self)
        self.edit_input.setPlainText("请输入要发送的内容")
        self.edit_input.setGeometry(220, 40, 250, 100)

    def text_output(self):
        self.edit_output = QTextEdit(self)
        self.edit_output.setPlainText("接收的内容")
        self.edit_output.setGeometry(220, 200, 250, 100)

    def print_device_info(self):
        index = self.combobox.currentIndex()
        self.ProductID = self.devices[index]['product_id']
        self.VendorID = self.devices[index]['vendor_id']
        print(self.ProductID)

    def text_contain(self):
        pass

    def hid_info_box_init(self):
        self.pid_label = QLabel(self)
        self.pid_label.setText("PID:")
        self.pid_label.setFixedHeight(20)  # 设置高度为20像素

        self.vid_label = QLabel(self)
        self.vid_label.setText("VID:")
        self.vid_label.setFixedHeight(20)  # 设置高度为20像素


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_widget = MyWidget("hid")
    my_widget.show()
    sys.exit(app.exec_())
