#que obtenga el promedio de n numeros ingresados

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()

acu:float=0.0
def suma():
    global acu
    acu=float(acu)+float(num.value)
    num.value=""

def promedio():
    resultado=str(float(acu)/float(n.value))
    cadena=f"el promedio es {resultado}"
    engine.say(cadena)
    engine.runAndWait()
    result.value=resultado

def mensaje():
    cadena="ingresa n numeros y guardalos uno por uno"
    engine.say(cadena)
    engine.runAndWait()


app=App(title="ICI app")

button=PushButton(app,text="instruciones", command=mensaje)
message = Text(app, text="cuantos numeros seran:")
n = TextBox(app, width=20,)
message2 = Text(app, text="ingresa un numero:")
num = TextBox(app, width=20,)
button2=PushButton(app,text="Agg otro numero", command=suma)
button3=PushButton(app,text="Promediar", command=promedio)
result= Text(app,text="")
app.display()