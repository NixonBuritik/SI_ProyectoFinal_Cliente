import base64
from ImageCode import imagesCode


class Code64:

    def __init__(self):
        self.ruta = any
        self.contador = any

    def code64(self, ruta, contador):
        image = open(ruta, 'rb')  # open binary file in read mode
        image_read = image.read()
        image_64_encode = base64.encodebytes(image_read)
        code = image_64_encode.decode('ascii')
        print("Encoding...")

        imagen = {
            'id': str(contador),
            'content': code
        }
        imagesCode.append(imagen)