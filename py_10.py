#calcular la suma de 5 numeros ingresados, entre 5 y 10 (inclusive).

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()

a=1
conta=0
def suma():
    global conta,a
    if int(num.value)>=5 and int(num.value)<=10:
        result.value=""
        conta= conta+int(num.value)
        a=a+1
        message.value=f"numero {a}:"
    else:
        result.value="numero fuera de rango"

    if a>5:
        cadena=f"la suma es {conta}"
        engine.say(cadena)
        engine.runAndWait()
        result.value=f"la suma es {str(conta)}"
    else:
        num.value=""

def mensaje():
    cadena="ingresa y guarda los 5 numeros uno por uno"
    engine.say(cadena)
    engine.runAndWait()

app=App(title="ICI app")

button=PushButton(app,text="instruciones", command=mensaje)
message = Text(app, text=f"numero {a}:")
num = TextBox(app, width=20,)
button2=PushButton(app,text="siguiente numero", command=suma)
result= Text(app,text="")
app.display()