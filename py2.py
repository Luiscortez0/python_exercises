#se desea calcular la edad aprox de una persona pregruntando su año de nacimiento y el actual

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()

def calcular_edad():
    edad=str(int(aa.value)-int(an.value))
    cadena=f"tienes aproximadamente {edad} años"
    engine.say(cadena)
    engine.runAndWait()
    result.value=f"tienes {str(edad)} años"

app=App(title="ICI app")

message = Text(app, text="año de nacimiento:")
an = TextBox(app, width=20,)
message = Text(app, text="año actual:")
aa = TextBox(app, width=20,)
button=PushButton(app,text="Calcular edad", command=calcular_edad)
result= Text(app,text="")
app.display()