
import sys
import hid



def receive_hid_messages():
    try:
        hid_device = hid.device()
        #hid_device.open(1155,22352)
        device_path = br'\\?\HID#VID_0483&PID_5750&Col01#7&189eb17&0&0000#{4d1e55b2-f16f-11cf-88cb-001111000030}\KBD'
        hid_device.open_path(device_path)

        # hid_device.set_nonblocking(0)
        while True:
            data = hid_device.read(64)  # 一次最多读取64字节的数据
            if data:
                # 处理接收到的数据，data是一个字节数组
                print("Received data:", data)
                # 在这里执行你的处理逻辑
            else:
                # 如果没有数据，可以做其他操作或休眠一段时间
                print("no data")

    except Exception as e:
        print("Exception:", str(e))
    finally:
        try:
            hid_device.close()
        except:
            pass


if __name__ == '__main__':
    receive_hid_messages()

# if __name__ == '__main__':
#     hid_device=hid.device()
#     hid_devices=hid.enumerate()
#     for device_info in hid_devices:
#         if device_info['vendor_id'] == 1155 and device_info['product_id'] == 22352:
#            print("path:%s"% device_info['path'])
#            path=device_info['path']
#     hid_device.open(1155,22352)
#
#     print("Manufacturer: %s" % hid_device.get_manufacturer_string())
#     print("Product:{}".format(hid_device.get_product_string()))
#     print(f"My Serial is {hid_device.get_serial_number_string()}")
#
#     hid_device.set_nonblocking(1)
#     hid_device.write(0x01)
