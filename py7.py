#se desea obtener el cuadrado de un numero tecleado.

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()

def mensaje_cuadrado():
    resultado=str(int(name.value)**2)
    cadena=f"el cuadrado de {name.value} es {resultado}"
    engine.say(cadena)
    engine.runAndWait()
    result.value=str(resultado)

def mensaje():
    cadena="ingresa un numero entero positivo"
    engine.say(cadena)
    engine.runAndWait()

app=App(title="ICI app")

button=PushButton(app,text="instruciones", command=mensaje)
message = Text(app, text="Dame un numero")
name = TextBox(app, width=20,)
button2=PushButton(app,text="Calcular cuadrado", command=mensaje_cuadrado)
result= Text(app,text="")
app.display()