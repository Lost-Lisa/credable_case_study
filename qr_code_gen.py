#qr_code_gen
import qrcode
# example data
data = "25635265,1PM 1 Jan,6PM 6 Jan,Air,BlueDart,856.50,15245254,Paid"
# output file name
filename = "site.png"
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)