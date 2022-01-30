from deepface import DeepFace
import cv2
import numpy as npy
import matplotlib.pyplot as plott
print("----------------------------------------------------\n")

programname= "Depression Asisstant GDSC Solution"
devdate= "26 January 2022"
devby= "Developed by Tech Futuristic Team"
print(programname)
print(devdate)
print(devby)

print("----------------------------------------------------\n")

class Menu_DepAs():
    def MenuDepAs():
        print("Menu Depression Asisstant:\n")
        print
        print("1.Start analyz emotion")
        print("2.Exit")


class Analyz():
    def analyz(self):
        print("You're choose analyz emotion\n")
        face_person = "rhaina_ngeselin.jpg"
        an_face = DeepFace.analyze(face_person, actions = ['emotion'])
        plott.imshow(face_person[:,:,::-1])
        
        print(an_face)
        webcam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        while True:
            _, openwebcam = webcam.read()
            img = im = Image.fromarray(openwebcam, 'RGB')
            img = img.resize((128, 128))
            img_array = np.array(img)
            img_array = np.expand_dims(img_array, axis=0)
            frameCopy= openwebcam.copy()
            frameCopy = cv2.resize(frameCopy, (120, 320))
            gray = cv2.cvtColor(frameCopy, cv2.COLOR_BGR2GRAY)
            img_array = np.array(gray)
            img_array = img_array.reshape(120, 320, 1)
            img_array = np.expand_dims(img_array, axis=0)

            OpenAsisstant = DeepFace.analyze(img_array[0][0], actions = ['emotion'])

            if actions == 'fear':
                openwebcam = cv2.cvtColor(openwebcam, cv2.COLOR_BGR2GRAY)
                print("You're Sad,please take a nap today")

            if actions == 'happy':
                print("What's happend you?")


            if actions == 'disgust':
                print("Hey,please don't be angry, stay a be calm")
            
            cv2.imshow("Depression Assistant",openwebcam)

            print(OpenAsisstant)

            hotkeys_quit = cv2.waitKey(1)

            if hotkeys_quit == ord('q'):
                break

            webcam.release()
            cv2.destroyAllWindows()
            
            
        

class Exitss():
    def exitss(self):
        print("Thanks for using ^-^\n")
        print("Good bye\n")
        exit

Menu_DepAs.MenuDepAs()

ch= int(input("Please,choose number on menu:"))
An = Analyz()
Ex = Exitss()

if ch== 1:
    An.analyz()
elif ch== 2:
    Ex.exitss()
else:
    print("Sorry, your choose not already exist")
    exit
