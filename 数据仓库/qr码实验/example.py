import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.make(fit=True)
qr.add_data("https://www.jxnu.edu.cn/")

img = qr.make_image(fill_color='blue', back_color='pink')

img.show()