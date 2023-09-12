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
        self.hid_info_box_init()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.resize(500, 500)
        self.move(500, 200)

        layout.addWidget(self.combobox)
        layout.addWidget(self.hid_info_box)

    def combobox_init(self):
        self.combobox = QComboBox(self)
        self.combobox.setGeometry(20, 40, 170, 30)
        self.devices = hid.enumerate()  # 打印 HID 设备
        self.combobox.currentIndexChanged.connect(self.print_device_info)
        temp_devices = []
        for device in self.devices:
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
        self.edit_input = QTextEdit(self)
        self.edit_input.setPlainText("请输入要发送的内容")
        self.edit_input.setGeometry(220, 40, 250, 100)

    def text_output(self):
        self.edit_out = QTextEdit(self)
        self.edit_out.setPlainText("接收的内容")
        self.edit_out.setGeometry(220, 200, 250, 100)

    def print_device_info(self):
        index = self.combobox.currentIndex()
        self.ProductID = self.devices[index]['product_id']
        self.VendorID = self.devices[index]['vendor_id']
        print(self.ProductID)

    def btn_open_click(self):
        try:

            hid.Device().open(self.ProductID, self.VendorID)  # TREZOR VendorID/ProductID
            print("ProductID:", self.ProductID)
            print("VendorID:", self.VendorID)
            print("Manufacturer: %s" % self.h.get_manufacturer_string())
            print("Product: %s" % self.h.get_product_string())
            print("Serial No: %s" % self.h.get_serial_number_string())

            self.h.set_nonblocking(1)


        # self.h.open()  # TREZOR VendorID/ProductID
        except Exception as e:
            # 捕获其他可能的异常
            error_message = str(e)
            print("Exception:", error_message)
            # 在页面展示错误或采取其他适当的措施
        except IOError as ex:
            print(ex)
            print("You probably don't have the hard-coded device.")
            print("Update the h.open() line in this script with the one")
            print("from the enumeration list output above and try again.")

    def btn_send_click(self):
        try:
            if self.h is not None:
                # 从文本框获取要发送的数据并转换为字节数组
                input_text = self.edit_input.toPlainText()
                data_to_send = input_text.encode('utf-8')
                self.h.write(data_to_send)
                print("发送成功")
                print(data_to_send)
            else:
                print("请打开端口")
        except Exception as e:
            # 捕获其他可能的异常
            error_message = str(e)
            print("Exception:", error_message)
            # 在页面展示错误或采取其他适当的措施

    def text_contain(self):
        pass

    def hid_info_box_init(self):

        self.hid_info_box = QVBoxLayout()
        self.hid_info_box.setContentsMargins(20, 0, 0, 0)# 左上右下


        pid_label=QLabel("ProductID:")
        pid_label.setFixedHeight(20)  # 设置高度为20像素
        self.hid_info_box.addWidget(pid_label)
        vid_label=QLabel("VendorID:")
        pid_label.setFixedHeight(20)  # 设置高度为20像素
        self.hid_info_box.addWidget(vid_label)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_widget = MyWidget("hid")
    my_widget.show()
    sys.exit(app.exec_())
