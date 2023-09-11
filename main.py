import hid
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QComboBox, QVBoxLayout, QPushButton, QTextEdit, QLabel


class MyWidget(QWidget):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.combobox_init()
        self.button_init()
        self.text_input()
        self.text_output()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.resize(500, 500)
        self.move(500, 200)

        layout.addWidget(self.combobox)

    def combobox_init(self):
        self.combobox = QComboBox(self)
        self.combobox.setGeometry(20, 40, 170, 30)
        self.devices = hid.enumerate()  # 打印 HID 设备
        self.combobox.currentIndexChanged.connect(self.print_device_info)
        temp_devices = []
        for device in self.devices:
            if device['product_string'] not in temp_devices:
                temp_devices.append(device['product_string'])
                self.combobox.addItem(device['product_string'])

    def button_init(self):
        self.btn_open = QPushButton("打开端口")
        self.btn_open.setGeometry(30, 100, 80, 40)
        self.btn_open.setParent(self)

        self.but_send = QPushButton("发送")
        self.but_send.setParent(self)
        self.but_send.setGeometry(280, 150, 80, 40)

        self.btn_open.clicked.connect(self.btn_open_click)
        self.but_send.clicked.connect(self.btn_send_click)

    def text_input(self):
        self.edit = QTextEdit(self)
        self.edit.setPlainText("请输入要发送的内容")
        self.edit.setGeometry(220, 40, 250, 100)

    def text_output(self):
        self.edit_out = QTextEdit(self)
        self.edit_out.setPlainText("接收的内容")
        self.edit_out.setGeometry(220, 200, 250, 100)

    def print_device_info(self):
        index = self.combobox.currentIndex()
        self.ProductID = hid.enumerate()[index]['product_id']
        self.VendorID = hid.enumerate()[index]['vendor_id']
        print(self.ProductID)

    def btn_open_click(self):
        try:
            self.h = hid.Device(vid=self.VendorID, pid=self.ProductID)
            self.h.open()  # TREZOR VendorID/ProductID
        except Exception as e:  # Traceback (most recent call last): :
            error_message = str(e)
            # 在页面展示错误
            # 创建一个标签控件
            open_error_label = QLabel(error_message, self)
            # 设置标签的位置和大小
            open_error_label.setGeometry(300, 300, 200, 30)
            print(error_message)

        print("ProductID:", self.ProductID)
        print("VendorID:", self.VendorID)

    def btn_send_click(self):
        # 发送数据
        data = [0x01, 0x02, 0x03]  # 要发送的数据
        self.h.write(data)
        # 接收数据
        print(data)
        data = self.h.read(64)  # 一次最多读取64字节的数

    def text_contain(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_widget = MyWidget("hid")
    my_widget.show()
    sys.exit(app.exec_())
