#que muestre un mensaje

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()

def mensaje():
    cadena=message.value
    engine.say(cadena)
    engine.runAndWait()

app=App(title="ICI app")

message = Text(app, text="Hola usuario")
button=PushButton(app,text="leer", command=mensaje)
app.display()