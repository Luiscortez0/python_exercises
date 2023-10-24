# la fime quiere dar una beca a su mejor estudiante, para eso le pregunto
# sus 6 calificaciones y su nombre, imprimir el nombre y promedio de la persona que gano la beca.

from guizero import App, Text, TextBox, PushButton
import pyttsx3
engine=pyttsx3.init()

def resultado():
    global nommax, promax
    cadena=f"El estudiante {nommax} gano la beca con un promedio de {promax}"
    engine.say(cadena)
    engine.runAndWait()
    result.value=f"El estudiante {nommax} gano la beca"
    result2.value=f"con un promedio de {promax}"

promax=0.0
nommax=""
def agg():
    global nommax, promax
    promedio= float(calf1.value)+float(calf2.value)+float(calf3.value)+float(calf4.value)+float(calf5.value)+float(calf6.value)
    promedio= promedio/6.0
    if promedio >promax:
        promax=promedio
        nommax=name.value
        
    calf1.value=""
    calf2.value=""
    calf3.value=""
    calf4.value=""
    calf5.value=""
    calf6.value=""
    name.value=""

def mensaje():
    cadena="ingresa el nombre y las 6 calificaciones de los estudiantes uno por uno"
    engine.say(cadena)
    engine.runAndWait()

app=App(title="ICI app")

button=PushButton(app,text="instruciones", command=mensaje)
message = Text(app, text="nombre:")
name = TextBox(app, width=20,)
message2 = Text(app, text="calificacion 1:")
calf1 = TextBox(app, width=20,)
message3 = Text(app, text="calificacion 2:")
calf2 = TextBox(app, width=20,)
message4 = Text(app, text="calificacion 3:")
calf3 = TextBox(app, width=20,)
message5 = Text(app, text="calificacion 4:")
calf4 = TextBox(app, width=20,)
message6 = Text(app, text="calificacion 5:")
calf5 = TextBox(app, width=20,)
message7 = Text(app, text="calificacion 6:")
calf6 = TextBox(app, width=20,)
button2=PushButton(app,text="Agg estudiante", command=agg)
button3=PushButton(app,text="terminar:", command=resultado)
result= Text(app,text="")
result2= Text(app,text="")
app.display()