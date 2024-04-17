import cv2
from deepface import DeepFace
import os

arquivos = os.listdir()

for arquivo in arquivos:
    if 'jpg' in arquivo:
        imagem = cv2.imread(arquivo)
        resultado = DeepFace.analyze(imagem, actions=('age', 'emotion', 'gender'))
        print(resultado)
