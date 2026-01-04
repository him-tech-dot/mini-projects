# import qrcode

# url = input("\nEnter your url : ")
# filename = input("File name to save it as : ")

# if not(filename.endswith(".png")):
#     filename = filename + ".png"


# img = qrcode.make(url)
# img.save(filename)

import qrcode

url = input("\nEnter the url : ")
filename = input("\nEnter filename to be saved as : ")

if not(filename.endswith("png")):
    filename = filename + ".png"

qr = qrcode.QRCode(
    version = None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(
    fill_color="white",
    back_color="black"
)
img.save(f"{filename}")
print("\n QR code succesfully generated")