# se desea imprimir un dia de la semana con respecto de un numero del 1 al 7.

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()

def dias():
    if int(n.value)==1:
        result.value="Dia lunes"
        engine.say(result.value)
        engine.runAndWait()
    elif int(n.value)==2:
        result.value="Dia martes"
        engine.say(result.value)
        engine.runAndWait()
    elif int(n.value)==3:
        result.value="Dia miercoles"
        engine.say(result.value)
        engine.runAndWait()
    elif int(n.value)==4:
        result.value="Dia jueves"
        engine.say(result.value)
        engine.runAndWait()
    elif int(n.value)==5:
        result.value="Dia viernes"
        engine.say(result.value)
        engine.runAndWait()
    elif int(n.value)==6:
        result.value="Dia sabado"
        engine.say(result.value)
        engine.runAndWait()
    elif int(n.value)==7:
        result.value="Dia domingo"
        engine.say(result.value)
        engine.runAndWait()
    else:
        result.value="Numero no valido"
        engine.say(result.value)
        engine.runAndWait()
        n.value=""

def mensaje():
    cadena="ingresa un numero del 1 al 7"
    engine.say(cadena)
    engine.runAndWait()


app=App(title="ICI app")

button=PushButton(app,text="instruciones", command=mensaje)
message = Text(app, text="ingresa un numero:")
n = TextBox(app, width=20,)
button2=PushButton(app,text="A que dia pertenece", command=dias)
result= Text(app,text="")
app.display()