import os
import qrcode
import pyzbar.pyzbar as pyzbar
from PIL import Image

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        # Read the QR code from the image
        img = Image.open(filename)
        data = pyzbar.decode(img)

        # Extract the decoded data
        data = data[0].data.decode()

        # Regenerate the QR code from the decoded data
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=12,
            border=1,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Save the regenerated QR code to the same file
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
