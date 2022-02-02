from deepface import DeepFace


print("----------------------------------------------------\n")

programname= "Depression Asisstant GDSC Solution"
devdate= "26 January 2022"
devby= "Developed by Tech Futuristic Team"
print(programname)
print(devdate)
print(devby)

print("----------------------------------------------------\n")

print("Welcome to Depression Assistant ^-^")

#database is folder data model face emotion
an_emot = DeepFace.stream("database", model_name='DeepFace') #Analyze Emotion from face with using library DeepFace
print(an_emot)









