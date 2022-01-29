from deepface import DeepFace
import cv2
import numpy as npy

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
        sad_person_path = ""
        happy_person_path = ""
        angry_person_path = ""
        verify_emotion = DeepFace.verify(sad_person_path = "",happy_person = "", angry_person_path = "")
        print(verify_emotion)
        an_face = DeepFace.analyze(sad_person_path = "",happy_person = "", angry_person_path = "", actions = ['emotion'])
        print(an_face)
        webcam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        while True:
            _, openwebcam = webcam.read()
            img = im = Image.fromarray(openwebcam, 'RGB')
            img = img.resize((128, 128))
            img_array = np.array(img)
            img_array = np.expand_dims(img_array, axis=0)
            frameCopy=openwebcam.copy()
            frameCopy = cv2.resize(frameCopy, (120, 320))
            gray = cv2.cvtColor(frameCopy, cv2.COLOR_BGR2GRAY)
            img_array = np.array(gray)
            img_array = img_array.reshape(120, 320, 1)
            img_array = np.expand_dims(img_array, axis=0)

            cv2.imshow("Depression Assistant",openwebcam)
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
