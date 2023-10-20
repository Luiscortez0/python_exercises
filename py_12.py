# se desea generar una secuencia de "0" y "1" pidiendo la longitud de la misma.

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()

b=0
conca=""
def imprimir():
    global b, conca
    for i in range(0,int(long.value)):
        if b==0:
            conca = conca + str(b) + ", "
            b=1
        else:
            conca = conca + str(b) + ", "
            b=0

    engine.say(conca)
    engine.runAndWait()
    result.value=conca

def mensaje():
    cadena="ingresa la longitud que deseas que tenga la secuencia"
    engine.say(cadena)
    engine.runAndWait()

app=App(title="ICI app")

button=PushButton(app,text="instruciones", command=mensaje)
message = Text(app, text="longitud:")
long = TextBox(app, width=20,)
button=PushButton(app,text="mostrar", command=imprimir)
result= Text(app,text="")
app.display()