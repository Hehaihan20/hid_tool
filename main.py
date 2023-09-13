import hid
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QComboBox, QVBoxLayout, QPushButton, QTextEdit, QLabel

import ui_hid
from ui_hid import MyWidget


class MyHid(MyWidget):
    def __init__(self, parent=None):
        super(MyHid, self).__init__(parent)
        self.connected = False
        self.devices = None
        self.Manufacturer = None
        self.Serial_no = None
        self.latest_device = None
        self.VendorID = None
        self.ProductID = None

        self.combobox_connect()
        self.btn_click()

    def combobox_connect(self):
        self.devices = hid.enumerate()
        for device in self.devices:
            self.combobox.addItem(device['product_string'])
        self.combobox.currentIndexChanged.connect(self.print_device_info)

    def btn_click(self):
        self.connect_button.clicked.connect(self.toggle_device)

        self.send_button.clicked.connect(self.send_info)

    def toggle_device(self):
        if self.connected:
            self.close_device()
        else:
            self.open_device()

    def print_device_info(self):
        index = self.combobox.currentIndex()
        self.ProductID = self.devices[index]['product_id']
        self.VendorID = self.devices[index]['vendor_id']
        print(self.devices[index])
        self.Manufacturer = self.devices[index]['manufacturer_string']
        self.Serial_number = self.devices[index]['serial_number']
        self.pid_label.setText("PID: " + str(self.ProductID))
        self.vid_label.setText("VID: " + str(self.VendorID))
        self.Manufacturer_label.setText("Manufacturer: " + str(self.Manufacturer))
        self.Serial_label.setText("Serial_number: " + str(self.Serial_number))

    def open_device(self):
        try:
            if self.VendorID is not None:
                self.connect_button.setCheckable(True)  # 设置按钮为可选中状态
                self.latest_device = hid.device()
                self.latest_device.open(self.VendorID, self.ProductID)  # 打开 HID 设备
                print("ProductID:", self.ProductID)
                print("VendorID:", self.VendorID)
                print("Manufacturer: %s" % self.latest_device.get_manufacturer_string())
                print("Product: %s" % self.latest_device.get_product_string())
                print("Serial No: %s" % self.latest_device.get_serial_number_string())
                self.connected = True
                self.latest_device.set_nonblocking(1)
            else:
                self.connected = False
                self.connect_button.setCheckable(False)  # 设置按钮为可选中状态


        except Exception as e:
            # 捕获其他可能的异常
            error_message = str(e)
            print("Exception:", error_message)
            self.status_label.setText(error_message)
            # 在页面展示错误或采取其他适当的措施
        except IOError as ex:
            print(ex)
            print("You probably don't have the hard-coded device.")
            print("Update the h.open() line in this script with the one")
            print("from the enumeration list output above and try again.")

    def close_device(self):
        self.latest_device.close()  # 打开 HID 设备
        self.connected = False
        print("close successfully")

    def send_info(self):
        try:
            if self.latest_device is not None:
                # 从文本框获取要发送的数据并转换为字节数组
                input_text = self.edit_input.toPlainText()
                data_to_send = input_text.encode('utf-8')
                self.latest_device.write(data_to_send)
                print("发送成功")
                self.status_label.setText("发送成功")
                print(data_to_send)
            else:
                self.status_label.setText("请打开端口")
                print("请打开端口")
        except Exception as e:
            # 捕获其他可能的异常
            error_message = str(e)
            self.status_label.setText(error_message)
            print("Exception:", error_message)
            # 在页面展示错误或采取其他适当的措施

    def text_contain(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_widget = MyHid("hid")
    my_widget.show()

    sys.exit(app.exec_())
