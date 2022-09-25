from queue import Empty
import cv2
import numpy as np

webcam = cv2.VideoCapture(0)
contador_matriculas = 0
cascade_matricula = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")

def GuardarMatricula(fotograma):
    global contador_matriculas
    cv2.imwrite(("matriculas\\"+str(contador_matriculas)+".jpg"), fotograma)
    contador_matriculas = contador_matriculas+1
    print("Guardado! numero:  " + str(contador_matriculas))

while(webcam.isOpened()):
    _, fotograma = webcam.read()

    #Convertimos imgagen a gris
    fotograma_gris = cv2.cvtColor(fotograma, cv2.COLOR_BGR2GRAY)
    #Detectar matriculas
    matriculas = cascade_matricula.detectMultiScale(fotograma_gris, 1.1, 5, minSize=(25,25))
    waitkey = cv2.waitKey(20)
    #Analizamos matriculas
    for matricula in matriculas:
        x = matricula[0]
        y = matricula[0]
        w = matricula[0]
        h = matricula[0]
        #Comprobamos area
        area = w*h
        if area > 100:   
            cv2.rectangle(fotograma, (x, y), (x+w, y+h), (255, 0, 0), thickness=3)
            imagen_recortada = fotograma[y:y+h, x:x+w]
            print(imagen_recortada)
            if not np.any(imagen_recortada) == None:

                cv2.imshow("Imagen recortada", imagen_recortada)
                if waitkey == ord("g"):
                    GuardarMatricula(imagen_recortada)


    cv2.imshow("Detector de matriculas", fotograma)
    waitkey = cv2.waitKey(20)

    if waitkey == ord("q"):
        break

cv2.destroyAllWindows()