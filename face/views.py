from distutils.util import execute

from django.shortcuts import render,redirect

from django.http import HttpResponse

import cv2

import numpy as np

import os

def detection(request):
        
    import cv2

    cap= cv2.VideoCapture(0)
    
    cap.read()
    
    import pickle
    
    file = open('important', 'rb')

    data = pickle.load(file)
  
    file.close()

    for i in data:

        model = cv2.face.LBPHFaceRecognizer_create()

        model.train(np.asarray(i[0]),np.asarray(i[1]))

        face_classifier = cv2.CascadeClassifier('C:/Users/hp/projet_python_reconaissance/face/haarcascade_frontalface_default.xml')

        def face_detector(img):

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_classifier.detectMultiScale(gray,1.3,5)

            if faces is():

                return img,[]

            for(x,y,w,h) in faces:

                cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)

                roi = img[y:y+h, x:x+w]

                roi = cv2.resize(roi, (200,200))

            return img,roi
        
        while True:

            ret, frame = cap.read()

            image, face = face_detector(frame)

            try:

                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                result = model.predict(face)

                if result[1] < 500:

                    confidence = int(100*(1-(result[1])/300))

                if confidence > 82:

                    request.session['cinid'] = i[2]
                    
                    return redirect("/recup_infos/recherche_detect")

                else:

                    break

            except:

                cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

                cv2.imshow('Face Cropper', image)

                pass

            if cv2.waitKey(1)==ord('q'):
        
                break
       
    cap.release()

    cv2.destroyAllWindows()
    
    return redirect("/ajouter")



def Dataset(request):
    
    face_classifier = cv2.CascadeClassifier('C:/Users/hp/projet_python_reconaissance/face/haarcascade_frontalface_default.xml')

    def face_extractor(img):

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = face_classifier.detectMultiScale(gray,1.3,5)

        if  faces is():

            return None

        for(x,y,w,h) in faces:

            cropped_face = img[y:y+h, x:x+w]

        return cropped_face
    
    cap = cv2.VideoCapture(0)

    count = 0

    nameID=request.session['cin'].lower()
    
    path='C:/Users/hp/projet_python_reconaissance/image/'+nameID

    os.makedirs(path)
            
    while True:

        ret, frame = cap.read()

        if face_extractor(frame) is not None:

            count+=1

            face = cv2.resize(face_extractor(frame),(200,200))

            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            file_name_path ='C:/Users/hp/projet_python_reconaissance/image/'+nameID+'/'+ str(count) + '.jpg'

            cv2.imwrite(file_name_path,face)

        else:

            print("Face not found")

            pass

        if cv2.waitKey(1)==ord('q') or count==100:

            break

    cap.release()

    cv2.destroyAllWindows()

    return redirect("/face/training")

def training(request):
        
        import pickle
        
        from os import listdir

        from os.path import isfile, join
        
        data_path = 'C:/Users/hp/projet_python_reconaissance/image/'

        data_path = data_path[0:len(data_path)]+request.session['cin']+'/'

        onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))]

        Training_Data, Labels = [], []

        for i, files in enumerate(onlyfiles):
            
            image_path = data_path + onlyfiles[i]
            
            images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            Training_Data.append(np.asarray(images, dtype=np.uint8))

            Labels.append(i)

        Labels = np.asarray(Labels, dtype=np.int32)

        data=[Training_Data,Labels,request.session['cin']]


        file = open('important', 'rb')
    
        big_data = pickle.load(file)   
    
        file.close()        

        big_data.append(data)
        
        file = open('important', 'wb')

        pickle.dump(big_data, file)

        file.close()

        return redirect('/sec')