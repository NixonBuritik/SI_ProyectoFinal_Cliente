import cv2
from Cropper import Cropper
from ImageCode import imagesCode
from Code64 import Code64
import requests

cropper = Cropper()
code64 = Code64()
camara = cv2.VideoCapture(1)
contador = 2


def dibujarContornos(imagen):
    #imagenGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    bordes = cv2.Canny(imagen, 200, 300)
    ctns, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #for c in ctns:
        #cv2.drawContours(imagen, [c], 0, (187, 47, 0), 2)

    return ctns,imagen


def enviarPeticion(id_client, models):

    params = {"id_client": id_client, "images": imagesCode, "models": models}
    response = requests.post('http://192.168.101.10:5000/predict', json=params)
    #response = requests.get('http://192.168.101.10:5000/models')
    print(response.text)


while True:
    _, imagen = camara.read()

    ctns, imagenContornos = dibujarContornos(imagen)

    # Para el programa
    k = cv2.waitKey(5) & 0xFF

    if k == 99:
        cropper.crop(imagen, ctns, contador)
        contador += 1
        print("------------------------Siguiente Objeto-----------------------------")

    cv2.imshow("Imagen camara", imagenContornos)

    if k == 101:
        for i in range(0, contador):
            code64.code64('Crops/crop_Object_'+ str(i) + '.jpg', str(i))

        id_client= 'Usuario1'
        models = ['modelo1']

        enviarPeticion(id_client, models)

    if k == 27:
        break

camara.release()
cv2.destroyAllWindows()