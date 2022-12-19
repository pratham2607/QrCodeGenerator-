import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color="white")
    img_name = input("Enter Qr code name")
    img.save(img_name+".png")

url = input("Enter your url: ")
generate_qrcode(url)
print("Congratulation your QR code has been generated!")