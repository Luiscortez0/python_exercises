# se desea calcular la suma de 3 numeros ingresados por teclado

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()

def suma():
    suma=str(int(n1.value)+int(n2.value)+int(n3.value))
    cadena=f"la suma es {suma}"
    engine.say(cadena)
    engine.runAndWait()
    result.value=f"la suma es {str(suma)}"

app=App(title="ICI app")

message = Text(app, text="numero 1:")
n1 = TextBox(app, width=20,)
message2 = Text(app, text="numero 2:")
n2 = TextBox(app, width=20,)
message3 = Text(app, text="numero 3:")
n3 = TextBox(app, width=20,)
button=PushButton(app,text="Sumar", command=suma)
result= Text(app,text="")
app.display()