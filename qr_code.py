import qrcode
from PIL import Image

# Place the logo that you want to use in the same folder and change this field to that image

logo_img = input('Enter logo name to add to QR code (leave blank for Tux the Penguin with a flag: ')

if logo_img == '':
	logo_img = 'tux_flag.png'


logo = Image.open(logo_img)

# taking base width
basewidth = 100

# adjust image size
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(version=4, error_correction=qrcode.constants.ERROR_CORRECT_H)

# Add data to QR code
data = input('Enter text data to put into the QR code: ')
print()
QRcode.add_data(data)

# generating QR code
QRcode.make()

ans = input("Would you like to add custom color to the QR code? y/n  (Note: this can make it more difficult to scan the QR code depending on the color combination): ")

QR_color = '#000'
QR_background_color = '#fff'


if ans == 'y' or ans == 'yes':
	# Add color data to QR code
	QR_color = input("Enter either a color name like 'red' or the hex value for the QR color like '#ff00aa': ")
	print()

	QR_background_color = input("Enter either a color name like 'red' or the hex value for the QR background color like '#ff00aa': ")
	print()


# adding color to QR code
QRimg = QRcode.make_image(fill_color=QR_color, back_color=QR_background_color).convert('RGB')

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
		(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# save the QR code generated
QRimg.save('QRCode.png')

print('QR Code successfully generated')
