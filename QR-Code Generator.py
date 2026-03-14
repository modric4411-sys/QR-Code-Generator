import qrcode
url = input("Enter your url: ")

img = qrcode.make(url)

img.save("qrcode.png")
print("QR Code Generated")
