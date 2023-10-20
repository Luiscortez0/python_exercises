#que obtenga el promedio de n edades preguntando el año de nacimiento y asumiendo que el actual es 2023

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()

aa=2023
acu:float=0.0
def suma():
    global acu, aa
    edad=int(aa)-int(an.value)
    acu=int(acu)+int(edad)
    an.value=""

def promedio():
    resultado=str(float(acu)/float(n.value))
    cadena=f"el promedio de las edades es {resultado}"
    engine.say(cadena)
    engine.runAndWait()
    result.value=resultado

def mensaje():
    cadena="ingresa n años de nacimiento y guardalos uno por uno"
    engine.say(cadena)
    engine.runAndWait()


app=App(title="ICI app")

button=PushButton(app,text="instruciones", command=mensaje)
message = Text(app, text="cuantas personas seran:")
n = TextBox(app, width=20,)
message2 = Text(app, text="ingresa el año de nacimiento:")
an = TextBox(app, width=20,)
button2=PushButton(app,text="Agg otra persona", command=suma)
button3=PushButton(app,text="Promediar edades", command=promedio)
result= Text(app,text="")
app.display()