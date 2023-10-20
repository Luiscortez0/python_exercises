#se desea calcular la suma de los cuadrados de n numero tecleados

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()

def resultado():
    global conta,conca
    cadena=f"la suma de los cuadrados es {conta}"
    engine.say(cadena)
    engine.runAndWait()
    result2.value=f"la suma es {conta}"

conta:int=0
conca="los cuadrados son: "
def suma():
    global conta,conca
    cuadrado=int(num.value)**2
    conta=conta+cuadrado
    conca= conca+","+str(cuadrado)
    num.value=""
    result.value=conca

def mensaje():
    cadena="ingresa n numeros y guardalos uno por uno"
    engine.say(cadena)
    engine.runAndWait()

app=App(title="ICI app")

button=PushButton(app,text="instruciones", command=mensaje)
message = Text(app, text="Dame un numero")
num = TextBox(app, width=20,)
button2=PushButton(app,text="Agg otro numero", command=suma)
button3=PushButton(app,text="terminar:", command=resultado)
result= Text(app,text="")
result2= Text(app,text="")
app.display()