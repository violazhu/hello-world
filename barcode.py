from pystrich.ean13 import EAN13Encoder
from pystrich.code128 import Code128Encoder
from io  import BytesIO
from PIL import Image

if __name__ == '__main__':
    # encoder = EAN13Encoder("690123456789")
    encoder=Code128Encoder("690123456789")#不同编码区别？
    #保存图片，并打开后print
    encoder.save("pyStrich.png")
    im = Image.open('pyStrich.png')
    im.show()

    #直接print
    fp = BytesIO()
    fp.write(encoder.get_imagedata())
    tmp = Image.open(fp)
    tmp.show()