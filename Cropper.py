import cv2


class Cropper:

    def __init__(self):
        self.image = any
        self.contours = []

    def crop(self,image, contours, contador):
        # cycles through all the contours to crop all
        for cntr in contours:
            # creates an approximate rectangle around contour
            x, y, w, h = cv2.boundingRect(cntr)
            # Only crop decently large rectangles
            #print('w' + str(w) + ' h' + str(h))
            if 200 < w < 330 and 200 < h < 440:
                #print('w'+str(w)+' h'+str(h))
                # pulls crop out of the image based on dimensions
                new_img = image[y:y + h, x:x + w]
                imagen = cv2.resize(new_img, (256, 256))
                imagenGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

                # writes the new file in the Crops folder
                cv2.imwrite('Crops/crop_Object_'+ str(contador) + '.jpg', imagenGris)
                #cv2.imwrite('Crops/1/1_' + str(contador) + '.jpg', imagen)
                # returns a number incremented up for the next file name
        return 1
