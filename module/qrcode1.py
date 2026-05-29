import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=40,
    border=4
)

qr.add_data("https://www.facebook.com/suzann.tamang.204773")
qr.make(fit=True)

q = qr.make_image(fill_color="black", back_color="white")

q.save("module/sujan.png")

print("QR Code Created")
