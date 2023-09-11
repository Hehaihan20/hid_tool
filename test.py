import hid
import sys


def contains(hid_devices, vendor_id, product_id):
    for device in hid_devices:
        if device['vendor_id'] not in vendor_id and device['product_id'] not in product_id:
            return device['vendor_id'], device['product_id']
    return -1

