import pyttsx3
engine = pyttsx3.init()
print("Robo Speaker 1.0 created by Yuvraj Singh")

while True:
    x = input("Enter what you want to speak: ")
    if x.lower() == "quit":
        print("Ok friend, bye bye")
        break
    engine.say(x)
    engine.runAndWait()
