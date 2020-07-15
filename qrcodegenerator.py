import pyqrcode as qr
import time
file = open("qr_text.txt" , "r")
names = file.readlines()
del names[-1]
for name in names:
    name = name[:-1]
    filename = ("qrcodes/"+ name + ".png")
    qrcode = qr.create(name)
    qrcode.png(filename,scale = 8 )
    print ( filename + " created")
    time.sleep(0.1)
