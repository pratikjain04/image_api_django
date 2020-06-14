from keras.models import load_model
import cv2
from minor.settings import MEDIA_URL
from django.conf import settings
import os

class Prediction:
    def cvModel(self):

        model = load_model(os.path.join(settings.BASE_DIR, 'computervision/my_model.h5'))

        # Reading the file in greyscale
        image = cv2.imread(MEDIA_URL + 'Y.jpg', 0)

        # Resizing the image according to the dimensions the network is trained on
        resized_image = cv2.resize(image, (28, 28))

        # Reshaping the image so that it's accepted by the model
        resized_image = resized_image.reshape(1, 28, 28, 1)

        # Prediction from our model
        pred = model.predict(resized_image)

        # Converting the predicted list of numbers to the alphabet
        l = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
             "X", "Y"]

        # The final alphabet is stored in variable output
        for i in range(24):
            if pred[0][i] == 1:
                #    print(l[i])
                output = l[i]
                exit

        return output

