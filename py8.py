#se desea generar los nuemros pares del 0 al 20

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()


def pares():
    conca=""
    for i in range(0,22,2):
        conca=conca+"/"+str(i)

    engine.say(conca)
    engine.runAndWait()
    result.value=conca

app=App(title="ICI app")

message = Text(app, text="pares del 0 al 20")
button=PushButton(app,text="mostrar", command=pares)
result= Text(app,text="")
app.display()