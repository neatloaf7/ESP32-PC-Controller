import usb_cdc
usb_cdc.enable(console=True, data=False)
#WARNING: ESP32 S3 cannot support both serial lines open at once